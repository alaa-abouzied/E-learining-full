# Generated by Django 3.2.13 on 2022-08-06 18:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0002_student_course'),
        ('video', '0002_alter_video_url'),
    ]

    operations = [
        migrations.AddField(
            model_name='video',
            name='course',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='course.course'),
            preserve_default=False,
        ),
    ]
