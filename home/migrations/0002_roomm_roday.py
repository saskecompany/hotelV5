# Generated by Django 3.2.2 on 2021-08-12 02:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='roomm',
            name='roday',
            field=models.IntegerField(blank=True, null=True, verbose_name='_days of book'),
        ),
    ]
