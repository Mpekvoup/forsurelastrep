# Generated by Django 5.1.2 on 2024-10-14 05:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('startit_app', '0005_quest_slug_alter_quest_chislo'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='job',
            name='category',
        ),
        migrations.DeleteModel(
            name='Category',
        ),
        migrations.DeleteModel(
            name='Job',
        ),
    ]
