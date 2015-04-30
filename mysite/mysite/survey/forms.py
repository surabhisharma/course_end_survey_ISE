from mysite.survey import models as m
from django.forms import ModelForm

class adsForm(ModelForm):
     class Meta:
        model = m.ads

