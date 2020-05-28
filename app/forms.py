from django import forms
from .models import Task


class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        exclude = ('user',)
        fields = '__all__'
        # TODO: tirar do exclude depois só pra teste
