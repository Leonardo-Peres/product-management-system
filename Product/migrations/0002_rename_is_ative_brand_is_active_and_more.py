# Generated by Django 5.0 on 2024-10-20 20:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Product', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='brand',
            old_name='is_ative',
            new_name='is_active',
        ),
        migrations.RenameField(
            model_name='category',
            old_name='is_ative',
            new_name='is_active',
        ),
    ]
