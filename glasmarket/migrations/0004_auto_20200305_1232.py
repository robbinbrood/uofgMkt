# Generated by Django 2.2.3 on 2020-03-05 12:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('glasmarket', '0003_category'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={'verbose_name_plural': 'Categories'},
        ),
        migrations.RemoveField(
            model_name='product',
            name='id',
        ),
        migrations.AddField(
            model_name='category',
            name='id',
            field=models.AutoField(auto_created=True, default=0, primary_key=True, serialize=False, verbose_name='ID'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='product',
            name='product_id',
            field=models.IntegerField(default=0, primary_key=True, serialize=False),
        ),
        migrations.AddField(
            model_name='user',
            name='picture',
            field=models.ImageField(default=0, upload_to=''),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='category',
            name='category_name',
            field=models.CharField(max_length=128, unique=True),
        ),
    ]
