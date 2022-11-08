from django_bootstrap5.widgets import RadioSelectButtonGroup
from django import forms

from .models import DailyHealthCheck

class DailyHealthCheckForm(forms.ModelForm):

    class Meta :

        model = DailyHealthCheck

        fields = [
            'check1',
            'check2',
            'check3',
            'check4',
            'check5',
            'check6',
        ]

        widgets = {
            'check1' : RadioSelectButtonGroup(attrs={'class':''}),
            # 'check1': RadioSelectButtonGroup(attrs={
            #     'class': "form-control",
            #     'style': '',
            #     'placeholder': 'Name'
            #     }),
            'check2' : RadioSelectButtonGroup,
            'check3' : RadioSelectButtonGroup,
            'check4' : RadioSelectButtonGroup,
            'check5' : RadioSelectButtonGroup,
            'check6' : RadioSelectButtonGroup,
        }

