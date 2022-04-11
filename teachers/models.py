from django.contrib.auth.models import User
from django.db import models

# Create your models here.
from catalog.models import ClassRoom,  Subject, Language
from organizations.models import Organization
from role.models import Role


class TeacherProfile(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    organization = models.ForeignKey(Organization, verbose_name='Организация', on_delete=models.CASCADE)
    iin = models.IntegerField(verbose_name='ИИН', blank=True, null=True)
    phone_number = models.CharField('Телефон', max_length=15, blank=True, null=True)
    classroom = models.ManyToManyField(ClassRoom, verbose_name='Классы в которых преподает', related_name='teacher_class')
    subject = models.ManyToManyField(Subject, verbose_name='Предмет преподования', related_name='teacher_subject')
    language = models.ManyToManyField(Language, verbose_name='Язык преподование', related_name='teacher_language')
    created_date = models.DateTimeField("Дата создания", auto_now_add=True)
    edit_date = models.DateTimeField(
        "Дата редактирования",
        auto_now=True,
    )
    published = models.BooleanField("Опубликовать?", default=True)
    role = models.ManyToManyField(Role, verbose_name='Роль пользователя')
    role_setter = models.ForeignKey(User, verbose_name='Кто дал рол', on_delete=models.CASCADE, related_name='role_setter')

    def __unicode__(self):
        return self.user

    class Meta:
        verbose_name = 'Учитель'
        verbose_name_plural = 'Учителя'