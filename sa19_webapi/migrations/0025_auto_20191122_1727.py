# Generated by Django 2.2.7 on 2019-11-22 17:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0024_auto_20191122_1724'),
    ]

    operations = [
        migrations.DeleteModel(
            name='UserFavourite',
        ),
        migrations.AlterField(
            model_name='grazpoi',
            name='id',
            field=models.CharField(max_length=255, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='grazshop',
            name='id',
            field=models.IntegerField(primary_key=True, serialize=False),
        ),
    ]
