# # #app order
from rest_framework import routers

from api.teachers.views import TeacherViewSet

router = routers.DefaultRouter()

router.register('teacher', TeacherViewSet)
