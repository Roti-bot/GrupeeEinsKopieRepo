# Generated by Django 2.2.7 on 2019-11-22 16:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0014_auto_20191122_1634'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userfavourite',
            name='id',
        ),
        migrations.AlterField(
            model_name='userfavourite',
            name='user',
            field=models.CharField(max_length=255, primary_key=True, serialize=False),
        ),
    ]
