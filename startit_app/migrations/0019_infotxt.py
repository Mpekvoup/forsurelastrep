# Generated by Django 5.1.2 on 2024-10-18 03:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('startit_app', '0018_remove_smiths_chislo_remove_quest_chislo_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='infotxt',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, verbose_name='Описание')),
                ('info', models.CharField(max_length=255, verbose_name='Название адресса')),
            ],
            options={
                'verbose_name': 'Описание',
                'verbose_name_plural': 'Описание',
            },
        ),
    ]
