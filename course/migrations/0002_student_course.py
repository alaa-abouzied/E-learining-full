# Generated by Django 3.2.13 on 2022-08-05 15:40

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('course', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Student_Course',
            fields=[
                ('id', models.BigAutoField(auto_created=True,
                 primary_key=True, serialize=False, verbose_name='ID')),
                ('student_course_name', models.ManyToManyField(
                    related_name='student_course', to='course.Course')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT,
                 related_name='userCourse', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]