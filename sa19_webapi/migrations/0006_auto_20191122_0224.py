# Generated by Django 2.2.7 on 2019-11-22 02:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0005_auto_20191122_0159'),
    ]

    operations = [
        migrations.AlterField(
            model_name='grazpoi',
            name='id',
            field=models.CharField(max_length=255, primary_key=True, serialize=False),
        ),
    ]
