# Generated by Django 3.2.2 on 2021-09-28 20:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('stay', '0017_auto_20210928_1600'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='stay',
            options={'ordering': ('-bookat',)},
        ),
    ]
