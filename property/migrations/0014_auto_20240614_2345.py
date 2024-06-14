# Generated by Django 5.0.6 on 2024-06-14 20:45

from django.db import migrations


def fill_field_property(apps, shcema_epitor):
    Flat = apps.get_model('property', 'Flat')
    Owner = apps.get_model('property', 'Owner')
    for owner in Owner.objects.all():
        flat = Flat.objects.filter(owner=owner.owner)
        owner.property.set(flat)
        owner.save()

class Migration(migrations.Migration):

    dependencies = [
        ('property', '0013_owner_property'),
    ]

    operations = [
        migrations.RunPython(fill_field_property)
    ]