# Generated by Django 2.2 on 2019-04-09 17:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('listings', '0002_auto_20190409_2235'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='brand',
            field=models.CharField(choices=[('dell', 'dell'), ('apple', 'apple'), ('onepluse', 'onepluse'), ('hp', 'hp')], max_length=200),
        ),
        migrations.AlterField(
            model_name='product',
            name='display_size',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=2),
        ),
        migrations.AlterField(
            model_name='product',
            name='processor_spped',
            field=models.DecimalField(blank=True, decimal_places=1, max_digits=4),
        ),
        migrations.AlterField(
            model_name='product',
            name='storage',
            field=models.DecimalField(blank=True, decimal_places=1, max_digits=4),
        ),
        migrations.AlterField(
            model_name='product',
            name='sub_type',
            field=models.CharField(choices=[('Electronic_product', 'Electronic_product'), ('accessories', 'accessories')], max_length=100),
        ),
        migrations.AlterField(
            model_name='product',
            name='weight',
            field=models.DecimalField(blank=True, decimal_places=1, max_digits=6),
        ),
    ]
