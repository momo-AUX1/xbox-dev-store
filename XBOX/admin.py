from django.contrib import admin
from .models import Category, Product


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'hidden', 'created_at', 'updated_at')
    search_fields = ('name',)
    list_filter = ('hidden', 'created_at')

    actions = ['make_visible', 'make_hidden']

    def make_visible(self, request, queryset):
        queryset.update(hidden=False)
        self.message_user(request, "Selected categories are now visible.")
    make_visible.short_description = "Mark selected categories as visible"

    def make_hidden(self, request, queryset):
        queryset.update(hidden=True)
        self.message_user(request, "Selected categories are now hidden.")
    make_hidden.short_description = "Mark selected categories as hidden"

class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'hidden', 'created_at', 'updated_at')
    search_fields = ('name', 'description')
    list_filter = ('category', 'hidden', 'created_at')

    actions = ['make_visible', 'make_hidden']

    def make_visible(self, request, queryset):
        queryset.update(hidden=False)
        self.message_user(request, "Selected products are now visible.")
    make_visible.short_description = "Mark selected products as visible"

    def make_hidden(self, request, queryset):
        queryset.update(hidden=True)
        self.message_user(request, "Selected products are now hidden.")
    make_hidden.short_description = "Mark selected products as hidden"

admin.site.register(Category, CategoryAdmin)
admin.site.register(Product, ProductAdmin)
