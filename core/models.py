from django.db import models


class Departament(models.Model):
    name = models.CharField('Название', max_length=128)

    class Meta:
        verbose_name = 'Факультет'
        verbose_name_plural = 'Факультеты'

    def __str__(self):
        return self.name


class Student(models.Model):
    departament = models.ForeignKey('core.Departament', on_delete=models.CASCADE, null=True, blank=True, related_name='dep')
    lastName = models.CharField('Фамилия', max_length=128)
    name = models.CharField('Имя', max_length=128)
    group = models.IntegerField('Номер группы')
    numberOfRecord = models.IntegerField('Номер зачетной книжки')

    class Meta:
        ordering = ['-group']
        verbose_name = 'Студент'
        verbose_name_plural = 'Студенты'

    def __str__(self):
        return self.lastName


class Section(models.Model):
    name = models.CharField('Название', max_length=128)
    student = models.ManyToManyField('core.Student')

    class Meta:
        verbose_name = 'Секция'
        verbose_name_plural = 'Секции'

    def __str__(self):
        return self.name
