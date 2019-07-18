# Generated by Django 2.2.2 on 2019-07-18 14:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0005_auto_20190715_1346'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='character',
            name='affiliation',
        ),
        migrations.AddField(
            model_name='character',
            name='affiliation',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='core.Affiliation'),
            preserve_default=False,
        ),
    ]