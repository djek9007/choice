# # #app order
from rest_framework import routers

from api.order.views import OrderViewSet, StatusOrderViewSet, CommentViewSet

router = routers.DefaultRouter()
router.register('order', OrderViewSet)
router.register('status', StatusOrderViewSet)
router.register('comment', CommentViewSet)