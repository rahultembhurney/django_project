# Generated by Django 4.0.2 on 2022-02-28 17:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0007_remove_customer_store_custo_last_na_e6a359_idx_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='customer',
            old_name='given_name',
            new_name='first_name',
        ),
    ]
