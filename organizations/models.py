from django.db import models
from django.utils.translation import gettext_lazy as _
# Create your models here.
from catalog.models import Region, District, Locality, TerritorialAffiliation, Language


class Organization(models.Model):
    """Модель таблицы организации"""
    region = models.ForeignKey(Region, verbose_name='Область', on_delete=models.CASCADE)
    district = models.ForeignKey(District, verbose_name='Район', on_delete=models.CASCADE)
    locality = models.ForeignKey(Locality, verbose_name='Населенный пункт', on_delete=models.CASCADE)
    territoriAlaffiliation = models.ForeignKey(TerritorialAffiliation, verbose_name='Территориральная принадлежность', on_delete=models.CASCADE)
    language = models.ForeignKey(Language, verbose_name='Язык', on_delete=models.CASCADE)
    name = models.CharField(_('Наименование организации'), max_length=100,)

    created_date = models.DateTimeField("Дата создания", auto_now_add=True, blank=True, null=True)
    edit_date = models.DateTimeField(
        "Дата редактирования",
        auto_now_add=True,
        blank=True,
        null=True
    )
    published = models.BooleanField("Опубликовать?", default=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Организация"
        verbose_name_plural = "Организации"