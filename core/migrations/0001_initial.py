# Generated by Django 4.0.3 on 2022-03-12 10:10

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('lastName', models.CharField(max_length=128, verbose_name='Фамилия')),
                ('name', models.CharField(max_length=128, verbose_name='Имя')),
                ('group', models.IntegerField(verbose_name='Номер группы')),
                ('numberOfRecord', models.IntegerField(verbose_name='Номер зачетной книжки')),
            ],
        ),
    ]
