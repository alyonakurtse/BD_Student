from django.db import models


class Departament(models.Model):
    name = models.CharField('Название', max_length=128)

    def __str__(self):
        return self.name


class Student(models.Model):
    departament = models.ForeignKey('core.Departament', on_delete=models.CASCADE, null=True, blank=True)
    lastName = models.CharField('Фамилия', max_length=128)
    name = models.CharField('Имя', max_length=128)
    group = models.IntegerField('Номер группы')
    numberOfRecord = models.IntegerField('Номер зачетной книжки')

    def __str__(self):
        return self.lastName


class Section(models.Model):
    name = models.CharField('Название', max_length=128)
    student = models.ManyToManyField('core.Student')

    def __str__(self):
        return self.name
