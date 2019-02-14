from django.contrib import admin
from .models import katalog

my_model = [katalog]
admin.site.register(my_model)