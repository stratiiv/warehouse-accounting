# Generated by Django 4.2.2 on 2023-07-02 14:42

from django.db import migrations, models
import products.services


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0002_category_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='image',
            field=models.ImageField(upload_to='products', validators=[products.services.validate_image]),
        ),
        migrations.AlterField(
            model_name='product',
            name='preview',
            field=models.ImageField(blank=True, null=True, upload_to='products/previews'),
        ),
    ]
