# Generated by Django 4.0.1 on 2022-01-22 00:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('data', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='Enter first name', max_length=20, null=True, verbose_name='First name')),
                ('second_name', models.CharField(help_text='Enter second name', max_length=20, null=True, verbose_name='Second name')),
                ('username', models.CharField(help_text='Enter username', max_length=20, unique=True, verbose_name='Username')),
                ('password', models.CharField(help_text='Enter your password', max_length=20, verbose_name='Password')),
                ('age', models.IntegerField(help_text='Enter name', null=True, verbose_name='Age')),
                ('date_registered', models.DateTimeField(auto_now=True)),
                ('routes_climbed', models.ManyToManyField(help_text='Choose routes already climbed', to='data.Route', verbose_name='List of routes already climbed')),
            ],
        ),
    ]
