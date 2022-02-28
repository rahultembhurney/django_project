from random import choices
from tkinter import CASCADE
from django.db import models

# Create your models here.

'''We need to create or models in the following way:

1. class Collection() -  A Parent class containing all the products.
2. class Product() -  Contains indormation regarding thr Products.

There can be multiple products in a collection so we have to establish a many-to - one relation here

3. class Customer() -  Conatins Customer info e.g, "Name", "Membership Status", etc.
4. class Order() - Consists of purchase records and payment statuses.
5. class OrderItems() - Contains details of products orderded.
6. class Address() - conatins customer address.

A customer can have multiple addresses so we'll need to establish a many-to-many relationship.
Similarly, order can consist multiple order items so same as above.

7. class Cart()  -  This class contains items to be checked out.
8. class CartItem() - Conatins details of items in cart'''


class Promotion(models.Model):
    description = models.CharField(max_length=255)
    discount = models.FloatField()


class Collection(models.Model):
    title = models.CharField(max_length=255)
    featured_product = models.ForeignKey(
        'Product', on_delete=models.SET_NULL, null=True, related_name='+')


class Product(models.Model):
    product_name = models.CharField(max_length=255)
    slug = models.SlugField()
    description = models.TextField(max_length=255)
    unit_price = models.DecimalField(max_digits=6, decimal_places=2)
    inventory = models.IntegerField()
    last_update = models.DateTimeField(auto_now=True)
    collection = models.ForeignKey(Collection, on_delete=models.PROTECT)
    promotions = models.ManyToManyField(Promotion)


class Customer(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    phone = models.CharField(max_length=255)
    birth_date = models.DateField(null=True)

    membership_bronze = 'B'
    membership_gold = 'G'
    membership_silver = 'S'

    MEMBERSHIP_CHOICES = [
        (membership_silver, 'SILVER'),
        (membership_bronze, 'BRONZE'),
        (membership_gold, 'GOLD')
    ]

    membership_status = models.CharField(max_length=1, choices=MEMBERSHIP_CHOICES,
                                         default=membership_bronze)


class Order(models.Model):
    placed_at = models.DateTimeField(auto_now_add=True)

    PAYMENT_COMPLETE = 'C'
    PAYMENT_PENDING = 'P'
    PAYMENT_FAILED = 'D'

    PAYMENT_CHOICES = [
        (PAYMENT_COMPLETE, 'PAYMENT_COMPLETE'),
        (PAYMENT_FAILED, 'PAYMENT_DECLINED'),
        (PAYMENT_PENDING, 'PAYMENT_PENDING'),
    ]

    payment_status = models.CharField(max_length=1,
                                      choices=PAYMENT_CHOICES, default=PAYMENT_PENDING)
    customer = models.ForeignKey(Customer, on_delete=models.PROTECT)


class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.PROTECT)
    product = models.ForeignKey(Product, on_delete=models.PROTECT)
    quantity = models.PositiveSmallIntegerField()
    price = models.DecimalField(max_digits=6, decimal_places=2)


class Address(models.Model):
    street = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    zip = models.PositiveIntegerField(null=True)


class Cart(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)


class CartItem(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveSmallIntegerField()
