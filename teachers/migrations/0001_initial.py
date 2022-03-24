# Generated by Django 3.2.12 on 2022-03-23 05:08

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('catalog', '0006_classroom_parallesclass'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('organizations', '0002_alter_organization_language'),
    ]

    operations = [
        migrations.CreateModel(
            name='TeacherProfile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(max_length=255, verbose_name='ФИО')),
                ('iin', models.IntegerField(max_length=12, verbose_name='ИИН')),
                ('phone_number', models.CharField(blank=True, max_length=15, null=True, verbose_name='Телефон')),
                ('classroom', models.ManyToManyField(to='catalog.ClassRoom', verbose_name='Классы в которых преподает')),
                ('language', models.ManyToManyField(to='catalog.Language', verbose_name='Язык преподование')),
                ('organization', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='organizations.organization', verbose_name='Организация')),
                ('parallesclass', models.ManyToManyField(to='catalog.ParallesClass', verbose_name='Параллели в классах')),
                ('subject', models.ManyToManyField(to='catalog.Subject', verbose_name='Предмет преподования')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Учитель',
                'verbose_name_plural': 'Учителя',
            },
        ),
    ]
