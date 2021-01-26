from django.forms import ModelForm
from todo.models import todo_model


class todo_modelForm(ModelForm):
    class Meta:
        model = todo_model
        fields = ['Title', 'Description', 'Important']

