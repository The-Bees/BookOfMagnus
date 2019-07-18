# Generated by Django 2.2.2 on 2019-07-15 13:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_auto_20190621_1529'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='book',
            name='characters',
        ),
        migrations.AddField(
            model_name='book',
            name='dramatis_personae',
            field=models.ManyToManyField(related_name='dramatis_personae', to='core.Character'),
        ),
        migrations.AddField(
            model_name='book',
            name='primary_characters',
            field=models.ManyToManyField(related_name='primary_characters', to='core.Character'),
        ),
        migrations.AddField(
            model_name='book',
            name='series_no',
            field=models.PositiveIntegerField(default=0),
            preserve_default=False,
        ),
    ]