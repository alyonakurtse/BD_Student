from django.test import TestCase, Client
from django.urls import reverse

from core import models


class StudentModel(TestCase):

    def setUp(self):
        self.student = models.Student.objects.create(lastName='Галимзянова', name='Регина', group=23, numberOfRecord=3423)

    def testStr(self):
        self.assertEqual(
            str(self.student),
            'Галимзянова',
        )


class StudentSearchTestCase(TestCase):
    def setUp(self):
        self.client = Client()
        self.student1 = models.Student.objects.create(name='Маша', group=23, numberOfRecord=23453)
        self.student2 = models.Student.objects.create(name='Наташа', group=24, numberOfRecord=23433)

    def testWithoutParams(self):
        response = self.client.get(reverse('core:student_list'))
        self.assertEqual(200, response.status_code)
        self.assertSequenceEqual(
            list(response.context['object_list']),
            list(models.Student.objects.all()),
            'При поиске без параметров должны выводиться все студенты',
        )

    def testSearchByName(self):
        response = self.client.get(reverse('core:student_list'), data={'name': 'Маша'})
        self.assertEqual(1, response.context['object_list'].count())
        self.assertEqual(
            'Маша',
            response.context['object_list'].first().name,
        )
