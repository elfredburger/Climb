# Generated by Django 4.0.1 on 2022-02-03 04:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('data', '0004_alter_boulder_grade'),
    ]

    operations = [
        migrations.AddField(
            model_name='boulder',
            name='location',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='data.location', verbose_name='Локация'),
        ),
        migrations.AddField(
            model_name='boulder',
            name='sector',
            field=models.ForeignKey(default=1, max_length=30, on_delete=django.db.models.deletion.CASCADE, to='data.sector', verbose_name='Выберите сектор'),
        ),
        migrations.AlterField(
            model_name='route',
            name='grade',
            field=models.ForeignKey(default='Еще не известно', on_delete=django.db.models.deletion.SET_DEFAULT, to='data.grade', verbose_name='Сложность'),
        ),
    ]