# Generated by Django 4.2.11 on 2024-05-05 19:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('listapp', '0005_alter_list_options_list_complete_delete_item'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='list',
            options={'ordering': ['complete']},
        ),
    ]
