from django.contrib import admin
from .models import Doctor, User


@admin.register((Doctor))
class doctorAdmin(admin.ModelAdmin):
    list_display = ['Name', 'Degree', 'Contact',
                    'Email', 'Password', 'Image', 'Category']


@admin.register((User))
class userAdmin(admin.ModelAdmin):
    list_display = ['Name', 'Contact', 'Email', 'Password']
