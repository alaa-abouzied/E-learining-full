# Generated by Django 3.2.15 on 2022-08-10 03:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0004_rename_student_course_instructor_course_course_instructor'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cat_name', models.CharField(max_length=50)),
            ],
        ),
        migrations.AddField(
            model_name='course',
            name='course_category',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='course_category', to='course.category'),
        ),
    ]