# Generated by Django 2.2.7 on 2019-11-22 15:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0008_auto_20191122_1542'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userfavourite',
            name='search_radius',
            field=models.CharField(max_length=255),
        ),
    ]