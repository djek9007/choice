
from django import forms


from .models import Organization



class OrganizationForm(forms.ModelForm):

    class Meta:
        model = Organization
        fields = ('region', 'district', 'locality', 'territoriAlaffiliation', 'language', 'name',)

