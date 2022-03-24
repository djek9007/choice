from django.shortcuts import render

# Create your views here.
from django.views.generic.base import View


from .forms import OrganizationForm







class OrganizationsView(View):
    def get(self, request):
        form = OrganizationForm

        contex = {
            'form': form,
        }
        return render(request, 'organizations/create.html', contex)