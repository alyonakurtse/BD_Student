# Generated by Django 4.0.1 on 2022-03-13 11:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0007_alter_student_departament'),
    ]

    operations = [
        migrations.AlterField(
            model_name='section',
            name='student',
            field=models.ManyToManyField(to='core.Student'),
        ),
    ]