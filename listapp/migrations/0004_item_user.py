# Generated by Django 4.2.11 on 2024-05-05 17:35

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('listapp', '0003_remove_item_slug_remove_list_slug'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
