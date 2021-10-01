# Generated by Django 3.2.2 on 2021-09-26 14:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('home', '0003_remove_roomm_roday'),
        ('user', '0006_user_nname'),
    ]

    operations = [
        migrations.CreateModel(
            name='stay',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(blank=True, max_length=50, null=True, verbose_name='user name')),
                ('stay', models.IntegerField(blank=True, null=True, verbose_name='long stay')),
                ('brom', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='home.roomm', verbose_name='')),
                ('ipuser', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user.user', verbose_name='user ip')),
            ],
        ),
    ]
