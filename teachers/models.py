from django.contrib.auth.models import User
from django.db import models

# Create your models here.
from catalog.models import ClassRoom, ParallesClass, Subject, Language
from organizations.models import Organization


class TeacherProfile(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    organization = models.ForeignKey(Organization, verbose_name='Организация', on_delete=models.CASCADE)
    iin = models.IntegerField(verbose_name='ИИН')
    phone_number = models.CharField('Телефон', max_length=15, blank=True, null=True)
    classroom = models.ManyToManyField(ClassRoom, verbose_name='Классы в которых преподает')
    parallesclass = models.ManyToManyField(ParallesClass, verbose_name='Параллели в классах')
    subject = models.ManyToManyField(Subject, verbose_name='Предмет преподования')
    language = models.ManyToManyField(Language, verbose_name='Язык преподование')


    def __unicode__(self):
        return self.user

    class Meta:
        verbose_name = 'Учитель'
        verbose_name_plural = 'Учителя'