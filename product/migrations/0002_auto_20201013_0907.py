# Generated by Django 3.1.2 on 2020-10-13 09:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='condition',
            field=models.CharField(choices=[('New', 'New'), ('Used', 'Used')], max_length=200),
        ),
    ]
