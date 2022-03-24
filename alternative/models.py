from django.contrib.auth.models import User
from django.db import models

# Create your models here.
from publishingHouse.models import PublishingHouse, Subject, ClassRoom, YearPublising


class Alternative(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    publishingHouse = models.ForeignKey(PublishingHouse, verbose_name='Издательство', on_delete=models.CASCADE)
    subject = models.ForeignKey(Subject, verbose_name='Предмет', on_delete=models.CASCADE)
    classroom = models.ForeignKey(ClassRoom, verbose_name='Класс', on_delete=models.CASCADE)
    yearPublishing = models.ForeignKey(YearPublising, verbose_name='Год издание', on_delete=models.CASCADE)

    def __unicode__(self):
        return self.user

    class Meta:
        verbose_name = 'Выбранные учебники'
        verbose_name_plural = 'Выбранные учебники'