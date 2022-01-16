from django.contrib import admin

from .models import Book,Author,Address

# Register your models here.

class BookAdmin(admin.ModelAdmin):
    list_display = ["title", "rating"]

class AuthorAdmin(admin.ModelAdmin):
    list_display = ["name"]

class AddressAdmin(admin.ModelAdmin):
    list_display = ["street", "postal_code", "city"]


admin.site.register(Book, BookAdmin)
admin.site.register(Author, AuthorAdmin)
admin.site.register(Address, AddressAdmin)
