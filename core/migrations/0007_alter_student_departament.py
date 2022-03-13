# Generated by Django 4.0.3 on 2022-03-12 16:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0006_alter_student_options_alter_student_departament'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='departament',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='dep', to='core.departament'),
        ),
    ]