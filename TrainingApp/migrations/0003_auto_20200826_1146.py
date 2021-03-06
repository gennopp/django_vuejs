# Generated by Django 3.1 on 2020-08-26 06:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('TrainingApp', '0002_auto_20200823_2352'),
    ]

    operations = [
        migrations.RenameField(
            model_name='dish',
            old_name='dish_price',
            new_name='price',
        ),
        migrations.RenameField(
            model_name='restaurant',
            old_name='dish',
            new_name='dish_served',
        ),
        migrations.RemoveField(
            model_name='dish',
            name='dish_name',
        ),
        migrations.RemoveField(
            model_name='restaurant',
            name='restaurant_address',
        ),
        migrations.RemoveField(
            model_name='restaurant',
            name='restaurant_name',
        ),
        migrations.AddField(
            model_name='dish',
            name='name',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='restaurant',
            name='address',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='restaurant',
            name='name',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
