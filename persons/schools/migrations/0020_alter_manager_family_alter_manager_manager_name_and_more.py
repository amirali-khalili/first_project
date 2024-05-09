# Generated by Django 5.0.4 on 2024-05-09 12:39

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('schools', '0019_alter_student_books'),
    ]

    operations = [
        migrations.AlterField(
            model_name='manager',
            name='family',
            field=models.CharField(blank=True, max_length=25, null=True, verbose_name='family'),
        ),
        migrations.AlterField(
            model_name='manager',
            name='manager_name',
            field=models.CharField(default=1, max_length=100),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='manager',
            name='phone',
            field=models.CharField(blank=True, max_length=11, null=True, verbose_name='  phone '),
        ),
        migrations.AlterField(
            model_name='moderator',
            name='family',
            field=models.CharField(default=1, max_length=25, verbose_name='enter your family'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='moderator',
            name='schools',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='schools.schools'),
        ),
        migrations.AlterField(
            model_name='schools',
            name='name',
            field=models.CharField(default=2, max_length=100),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='student',
            name='books',
            field=models.ManyToManyField(to='schools.book', verbose_name='کتاب ها'),
        ),
        migrations.AlterField(
            model_name='student',
            name='name',
            field=models.CharField(max_length=25, verbose_name='enter your name'),
        ),
    ]