from rest_framework import viewsets, permissions


# Create your views here.
from order.models import Order, StatusOrder, Comment


class OrderViewSet(viewsets.ModelViewSet):
    """Модель таблицы заявок """
    queryset = Order.objects.filter(published=True)
    permissions = [permissions.AllowAny]


class StatusOrderViewSet(viewsets.ModelViewSet):
    """Модель статуса для заявок"""
    queryset = StatusOrder.objects.filter(published =True)
    permissions = [permissions.AllowAny]

class CommentViewSet(viewsets.ModelViewSet):
    """Модель для обоснование корректировки заявок"""

    queryset = Comment.objects.filter(published=True)
    permissions = [permissions.AllowAny]