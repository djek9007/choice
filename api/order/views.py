from rest_framework import viewsets, permissions


# Create your views here.
from api.order.serializers import OrderSerializer, StatusOrderSerializer, CommentSerializer
from order.models import Order, StatusOrder, Comment


class OrderViewSet(viewsets.ModelViewSet):
    """Модель таблицы заявок """
    queryset = Order.objects.filter(published=True)
    serializer_class = OrderSerializer



class StatusOrderViewSet(viewsets.ModelViewSet):
    """Модель статуса для заявок"""
    queryset = StatusOrder.objects.filter(published =True)
    serializer_class = StatusOrderSerializer


class CommentViewSet(viewsets.ModelViewSet):
    """Модель для обоснование корректировки заявок"""

    queryset = Comment.objects.filter(published=True)
    serializer_class = CommentSerializer
