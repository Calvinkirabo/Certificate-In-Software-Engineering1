from django.contrib import settings
from .models import info
from django.forms import DateField, ModelForm

class DataForm(ModelForm):
    dob = DateField(input_formats=settings.DATE_INPUT_FORMATS)
    class Meta:
       model = info
       fields = ['dob']