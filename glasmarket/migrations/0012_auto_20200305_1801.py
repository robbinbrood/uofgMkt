# Generated by Django 2.2.3 on 2020-03-05 18:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('glasmarket', '0011_auto_20200305_1540'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='slug',
            field=models.SlugField(default=''),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='listing',
            name='picture',
            field=models.ImageField(default=0, upload_to=''),
        ),
        migrations.AlterField(
            model_name='user',
            name='picture',
            field=models.ImageField(default=0, upload_to=''),
        ),
    ]
