"""customization of an admin panel for a project"""
from django.contrib import admin
from django.contrib.admin import ModelAdmin

from .models import Book


# pylint: disable=unused-argument


class BookAdmin(ModelAdmin):
    """class defining the looks of an admin panel"""

    fieldsets = [
        ('Książki:', {'fields': ['title', 'issue_date']}),
        (
            'Dane z serwera',
            {
                'fields': ['genre', 'author'],
                'description': (
                    'Dane pobierane automatycznie.'
                )
            }
        ),
        (
            'Dane od użytkownika',
            {
             'fields': ['rating', 'description'],
             'description':
                 'Te pola wypełnia użytkownik'
            }
        )
    ]
    readonly_fields = ['issue_date']

    @staticmethod
    def issue_year(obj):
        """method converting full date to a year"""
        return obj.issue_date.year

    @staticmethod
    def change_genre_to_something(modeladmin, request, queryset):
        """method that allow a generic way to change genre to something"""
        queryset.update(genre='Something')

    ordering = ['id']
    list_display = ['title', 'genre', 'issue_year']
    list_display_links = ['title']
    list_per_page = 4
    list_filter = ['genre']
    search_fields = ['title']
    actions = ['change_genre_to_something']


admin.site.register(Book, BookAdmin)
