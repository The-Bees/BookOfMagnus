# Generated by Django 2.2.2 on 2019-06-07 13:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_auto_20190607_1257'),
    ]

    operations = [
        migrations.AlterField(
            model_name='affiliation',
            name='legion',
            field=models.BooleanField(default=False),
        ),
    ]
