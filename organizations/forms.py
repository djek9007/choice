from django.forms import  ModelForm

from organizations.models import Organization


class  OrganizationForm(ModelForm):
    class Meta:
        model = Organization
        fields = "__all__"
