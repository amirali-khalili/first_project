# Generated by Django 5.0.4 on 2024-05-09 07:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('schools', '0017_alter_book_title'),
    ]

    operations = [
        migrations.AlterField(
            model_name='class_lesson',
            name='name',
            field=models.CharField(max_length=100, verbose_name='enter your class name'),
        ),
    ]