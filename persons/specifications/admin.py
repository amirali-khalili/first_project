from django.contrib import admin
from .models import Person
from .models import Address

admin.site.register(Person)
admin.site.register(Address)
