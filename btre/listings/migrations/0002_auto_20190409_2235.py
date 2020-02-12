# Generated by Django 2.2 on 2019-04-09 17:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('listings', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='brand',
            field=models.CharField(choices=[('apple', 'apple'), ('dell', 'dell'), ('onepluse', 'onepluse'), ('hp', 'hp')], max_length=200),
        ),
        migrations.AlterField(
            model_name='product',
            name='display_size',
            field=models.DecimalField(blank=True, decimal_places=1, max_digits=1),
        ),
        migrations.AlterField(
            model_name='product',
            name='processor',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='product',
            name='processor_spped',
            field=models.IntegerField(blank=True, default=0),
        ),
        migrations.AlterField(
            model_name='product',
            name='ram',
            field=models.IntegerField(blank=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='storage',
            field=models.DecimalField(blank=True, decimal_places=1, max_digits=2),
        ),
        migrations.AlterField(
            model_name='product',
            name='type',
            field=models.CharField(choices=[('Laptop', 'Laptop'), ('Mobile', 'Mobile')], max_length=200),
        ),
        migrations.AlterField(
            model_name='product',
            name='weight',
            field=models.DecimalField(blank=True, decimal_places=1, max_digits=1),
        ),
    ]