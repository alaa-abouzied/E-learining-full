# Generated by Django 3.2.13 on 2022-08-06 18:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('video', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='video',
            name='url',
            field=models.FileField(upload_to='', verbose_name='./media/video'),
        ),
    ]
