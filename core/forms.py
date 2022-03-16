from django import forms

import core.models


class StudentSearch(forms.Form):
    lastname = forms.CharField(label='Фамилия', required=False)
    group = forms.IntegerField(label='Группа', required=False, help_text='Номер группы')

    def clean(self):
        cleaned_data = self.cleaned_data
        group = cleaned_data.get('group')

        if group and (group > 45 or group < 11):
            raise forms.ValidationError('Значение группы должно быть в диапозоне 10<группа<45')
        return cleaned_data

    # def clean(self):
    #     return forms.ValidationError('Ошибка')


class StudentEdit(forms.ModelForm):
    class Meta:
        model = core.models.Student
        fields = '__all__'
