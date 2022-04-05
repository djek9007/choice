from django.contrib.auth.models import User
from django.db import models

# Create your models here.
from django.utils.translation import gettext_lazy as _

from catalog.models import Region, District, Locality
from organizations.models import Organization


class Role(models.Model):
    """Таблица ролей"""
    name = models.CharField(_('Наименование ролей'), max_length=100,)

    def __str__(self):
        return self.name


    class Meta:
        verbose_name = "Роль"
        verbose_name_plural = "Роли"



class RegionRole(models.Model):
    """Таблица роли для администраторов Области/города"""
    user = models.ForeignKey(User, verbose_name='Пользователь', on_delete=models.CASCADE)
    role = models.ForeignKey(Role, verbose_name='Выберите роль администратора', on_delete=models.CASCADE,)
    region_role = models.ForeignKey(Region, verbose_name='Выберите область/город', on_delete=models.CASCADE,
                                    related_name='region_role')

    created_date = models.DateTimeField("Дата создания", auto_now_add=True, blank=True, null=True)
    edit_date = models.DateTimeField(
        "Дата редактирования",
        auto_now_add=True,
        blank=True,
        null=True
    )
    published = models.BooleanField("Опубликовать?", default=True)

    def __str__(self):
        return self.role.name

    class Meta:
        verbose_name = "Администраторы области/города"
        verbose_name_plural = "Администраторы области/города"


class DistrictRole(models.Model):
    """Таблица роли для администраторов района"""
    user = models.ForeignKey(User, verbose_name='Пользователь', on_delete=models.CASCADE)
    role = models.ForeignKey(Role, verbose_name='Выберите роль администратора', on_delete=models.CASCADE, )
    region_role = models.ForeignKey(Region, verbose_name='Выберите область/город', on_delete=models.CASCADE,)
    district_role = models.ForeignKey(District, verbose_name='Выберите район', on_delete=models.CASCADE, related_name='district_role')
    created_date = models.DateTimeField("Дата создания", auto_now_add=True, blank=True, null=True)
    edit_date = models.DateTimeField(
        "Дата редактирования",
        auto_now_add=True,
        blank=True,
        null=True
    )
    published = models.BooleanField("Опубликовать?", default=True)

    def __str__(self):
        return self.role.name

    class Meta:
        verbose_name = "Администраторы района"
        verbose_name_plural = "Администраторы района"


class LocalityRole(models.Model):
    """Таблица роли для администраторов населенного пункта"""
    user = models.ForeignKey(User, verbose_name='Пользователь', on_delete=models.CASCADE)
    role = models.ForeignKey(Role, verbose_name='Выберите роль администратора', on_delete=models.CASCADE, )
    region_role = models.ForeignKey(Region, verbose_name='Выберите область/город', on_delete=models.CASCADE,)
    district_role = models.ForeignKey(District, verbose_name='Выберите район', on_delete=models.CASCADE)
    locality_role = models.ForeignKey(Locality, verbose_name='Выберите населенный пункт', on_delete=models.CASCADE, related_name='locality_role')
    created_date = models.DateTimeField("Дата создания", auto_now_add=True, blank=True, null=True)
    edit_date = models.DateTimeField(
        "Дата редактирования",
        auto_now_add=True,
        blank=True,
        null=True
    )
    published = models.BooleanField("Опубликовать?", default=True)

    def __str__(self):
        return self.role.name

    class Meta:
        verbose_name = "Администраторы населенного пункта"
        verbose_name_plural = "Администраторы населенного пункта"





    # organization_role = models.ForeignKey(Organization, verbose_name='Администратор организаций',
    #                                       on_delete=models.CASCADE, blank=True, null=True,
    #                                       related_name='organization_role')
