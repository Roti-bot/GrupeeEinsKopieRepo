# Generated by Django 2.2.7 on 2019-11-22 16:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0011_auto_20191122_1625'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userfavourite',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]
