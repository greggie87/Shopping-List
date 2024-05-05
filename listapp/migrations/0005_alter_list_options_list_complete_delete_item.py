# Generated by Django 4.2.11 on 2024-05-05 18:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('listapp', '0004_item_user'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='list',
            options={'ordering': ['-complete']},
        ),
        migrations.AddField(
            model_name='list',
            name='complete',
            field=models.BooleanField(default=False),
        ),
        migrations.DeleteModel(
            name='Item',
        ),
    ]
