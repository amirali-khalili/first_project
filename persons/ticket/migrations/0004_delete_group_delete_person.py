# Generated by Django 5.0.4 on 2024-05-08 14:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ticket', '0003_delete_membership'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Group',
        ),
        migrations.DeleteModel(
            name='Person',
        ),
    ]