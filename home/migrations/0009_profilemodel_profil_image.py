# Generated by Django 4.2.3 on 2023-09-21 11:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0008_projectmodel_project_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='profilemodel',
            name='profil_image',
            field=models.ImageField(blank=True, default='defult_avatar_png', null=True, upload_to='images/'),
        ),
    ]
