# Generated by Django 2.2.3 on 2020-03-11 18:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('glasmarket', '0024_auto_20200311_1843'),
    ]

    operations = [
        migrations.AlterField(
            model_name='listing',
            name='date',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
