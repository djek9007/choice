from django.contrib.auth.models import User
from django.db import models
from django.utils.translation import gettext_lazy as _
# Create your models here.
from catalog.models import ClassRoom, Language
from organizations.models import Organization
from publishingHouse.models import PublishingHouse

class StatusOrder(models.Model):
    """Модель таблицы статуса"""
    name = models.CharField(_('Статус'), max_length=100)
    created_date = models.DateTimeField("Дата создания", auto_now_add=True)
    edit_date = models.DateTimeField(
        "Дата редактирования",
        auto_now=True,
    )
    published = models.BooleanField("Опубликовать?", default=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Статус"
        verbose_name_plural = "Статусы"


class Order(models.Model):
    """Модель заявок из школ в МИО"""
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    organization = models.ForeignKey(Organization, verbose_name='Организация', on_delete=models.CASCADE)
    classroom = models.ForeignKey(ClassRoom, verbose_name='Класс', on_delete=models.CASCADE)
    language = models.ForeignKey(Language, verbose_name='Язык', on_delete=models.CASCADE)
    publishingHouse = models.ForeignKey(PublishingHouse, verbose_name='Издательство', on_delete=models.CASCADE)
    countTextBook = models.IntegerField(verbose_name='Количество')
    status = models.ForeignKey(StatusOrder, verbose_name='Статус', on_delete=models.CASCADE)
    sent_raiono = models.BooleanField(default=False, verbose_name='Отправить в РАЙОНО')
    sent_uoo = models.BooleanField(default=False, verbose_name='Отправить в УО')
    created_date = models.DateTimeField("Дата создания", auto_now_add=True,)
    edit_date = models.DateTimeField(
        "Дата редактирования",
        auto_now=True,
    )
    published = models.BooleanField("Опубликовать?", default=True)
    def __str__(self):
        return self.organization.name

    class Meta:
        verbose_name = 'Заявка'
        verbose_name_plural = 'Заявки'


class Comment(models.Model):
    """Модель для обоснование корректировки или отказа"""
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.TextField('Обоснование')
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='comments')
    created_date = models.DateTimeField("Дата создания", auto_now_add=True)

    edit_date = models.DateTimeField(
        "Дата редактирования",
        auto_now_add=True,
    )
    published = models.BooleanField("Опубликовать?", default=True)

    def __str__(self):
        return self.user.username

    class Meta:
        verbose_name = 'Обоснование'
        verbose_name_plural = 'Обоснования'



