# Generated by Django 3.2.11 on 2022-01-20 16:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("product", "0157_update_product_search_document"),
    ]

    operations = [
        migrations.AlterField(
            model_name="collection",
            name="name",
            field=models.CharField(max_length=250),
        ),
    ]