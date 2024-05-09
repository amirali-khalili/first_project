from django.contrib import admin

from.models import schools
from.models import class_Lesson
from.models import student
from.models import book
from.models import manager
from.models import Moderator

admin.site.register(schools)
admin.site.register(class_Lesson)
admin.site.register(student)
admin.site.register(book)
admin.site.register(manager)
admin.site.register(Moderator)
