# Generated by Django 5.1.2 on 2024-10-20 12:18

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('startit_app', '0020_remove_infotxt_info_infotxt_created_at_infotxt_slug_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='addresesq',
            name='quest',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='addresses', to='startit_app.quest', verbose_name='Квест'),
        ),
    ]