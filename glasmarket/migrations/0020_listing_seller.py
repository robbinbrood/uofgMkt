# Generated by Django 2.2.3 on 2020-03-08 09:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('glasmarket', '0019_auto_20200308_0045'),
    ]

    operations = [
        migrations.AddField(
            model_name='listing',
            name='seller',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='glasmarket.UserProfile'),
            preserve_default=False,
        ),
    ]
