# Generated by Django 5.0.4 on 2024-05-09 07:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('schools', '0015_alter_student_books'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='books',
            field=models.ManyToManyField(to='schools.book'),
        ),
    ]
