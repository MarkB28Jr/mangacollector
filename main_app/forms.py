from django.forms import ModelForm
from .models import ReadMe

class ReadMeForm(ModelForm):
  class Meta:
    model = ReadMe
    fields = ['date', 'read']