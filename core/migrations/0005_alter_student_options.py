# Generated by Django 4.0.3 on 2022-03-12 16:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_section'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='student',
            options={'ordering': ['group']},
        ),
    ]