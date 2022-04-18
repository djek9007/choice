from rest_framework import serializers

from order.models import Order, StatusOrder, Comment


class OrderSerializer(serializers.ModelSerializer):
    """Сериалайзер для модели заявок"""

    class Meta:
        model = Order
        fields = '__all__'

class StatusOrderSerializer(serializers.ModelSerializer):
    """Сериалайзер для модели статуса заявок"""

    class Meta:
        model= StatusOrder
        fields = '__all__'

class CommentSerializer(serializers.ModelSerializer):
    """Сериялайзер для модели обоснование корректировки заявки"""

    class Meta:
        model= Comment
        fields = '__all__'