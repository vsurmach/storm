# Generated by Django 4.0.5 on 2022-09-15 17:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lesson_3', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='FaceBook',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=30)),
                ('password', models.CharField(max_length=30)),
            ],
        ),
    ]
