from django.contrib import admin
from .models import Pets, Books

# Register your models here.


class PetsAdmin(admin.ModelAdmin):
    list_display = ["pid", "petname", "age", "description", "pimage"]


class BooksAdmin(admin.ModelAdmin):
    list_display = ["bookid", "title", "author", "price", "bimage"]


admin.site.register(Pets, PetsAdmin)
admin.site.register(Books, BooksAdmin)
