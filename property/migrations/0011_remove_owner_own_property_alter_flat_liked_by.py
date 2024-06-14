# Generated by Django 5.0.6 on 2024-06-14 20:29

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('property', '0010_alter_flat_liked_by_owner'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.RemoveField(
            model_name='owner',
            name='own_property',
        ),
        migrations.AlterField(
            model_name='flat',
            name='liked_by',
            field=models.ManyToManyField(blank=True, related_name='liked_appartment', to=settings.AUTH_USER_MODEL, verbose_name='Кто лайкнул'),
        ),
    ]