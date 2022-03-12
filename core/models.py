from django.db import models


class Student(models.Model):
    lastName = models.CharField('Фамилия', max_length=128)
    name = models.CharField('Имя', max_length=128)
    group = models.IntegerField('Номер группы')
    numberOfRecord = models.IntegerField('Номер зачетной книжки')

    def __str__(self):
        return self.lastName
