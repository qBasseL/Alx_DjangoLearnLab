from django.contrib import admin
from .models import Book
# Register your models here.

class BookAdmin(admin.ModelAdmin):
    list_display = ('author', 'title')
    list_filter = ('author', 'publication_year')
    
admin.site.register(Book, BookAdmin)