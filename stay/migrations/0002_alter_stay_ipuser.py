# Generated by Django 3.2.2 on 2021-09-26 14:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0006_user_nname'),
        ('stay', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='stay',
            name='ipuser',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='user.user', verbose_name='user ip'),
        ),
    ]