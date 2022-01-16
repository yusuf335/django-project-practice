from django.contrib import admin

from .models import Book, Author, Address, Country

# Register your models here.


class BookAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("title",)}
    list_filter = ("author", "rating")
    list_display = ("title", "author")
    list_per_page = (10)

class AddressAdmin(admin.ModelAdmin):
    list_display = ("street", "postal_code", "city")
    list_filter = ("postal_code", "city")


admin.site.register(Book, BookAdmin)
admin.site.register(Author)
admin.site.register(Address, AddressAdmin)
admin.site.register(Country)
