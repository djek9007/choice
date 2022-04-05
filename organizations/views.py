from rest_framework import viewsets


from .models import Organization
from .serializers import OrganizationSerializer


class OrganizationsViewSet(viewsets.ModelViewSet):
    """Модель Организации"""
    serializer_class = OrganizationSerializer
    queryset = Organization.objects.filter(published=True)


# class OrganizationListView(generics.ListAPIView):
#     """Вывод всех выбранных учебников"""



#
#
# class OrganizationCreateView(generics.CreateAPIView):
#     """Добавление выбранного алтернативного учебника"""
#     serializer_class = OrganizationCreateSerializers
#
#
# class OrganizationDetailView(generics.RetrieveUpdateDestroyAPIView):
#     """Вывод одного выбранного учебника, редактирование, удаление"""
#     serializer_class = OrganizationDetailSerializer
#
#     def get_queryset(self):
#         """Форма запроса из базы"""
#         organization = Organization.objects.filter(published=True)
#         return organization
#
#
# def load_distict(request):
#     region_id = request.GET.get('region')
#     district = Organization.objects.filter(district_id=region_id).order_by('name')
#     return render(request, 'hr/region_dropdown_list.html', {'region': district})
#
# class OrganizationView(View):
#     """Вывод категории и вывод стати"""
#
#     # запрос к базе по полю публикации на true
#     def get_queryset(self):
#         return Organization.objects.filter(published=True)
#
#     def get(self, request):
#         organizations = self.get_queryset()
#         form = OrganizationForm
#
#         context = {
#
#             'organizations': organizations,
#             'form':form,
#         }
#         return render(request, 'organizations/organization.html', context)
#
#     def post(self, request, **kwargs):
#         form = OrganizationForm(request.POST)
#         if form.is_valid():
#             form = form.save(commit=False)
#             form.save()
#         return redirect(request.path)

