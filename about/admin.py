from django.contrib import admin
from .models import About
from django_summernote.admin import SummernoteModelAdmin


admin.site.register(About)