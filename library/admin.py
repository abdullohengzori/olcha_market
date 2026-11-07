
from django.contrib import admin
from .models import User, Shop, Product

@admin.action(description="narhni 0 so'm qilish")
def narh(modeladmin, request, queryset):
    queryset.update(price=0)


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('last_name', 'username', 'first_name',)
    # list_display_links = ('username', 'first_name', 'last_name',)
    # readonly_fields = ('first_name', 'last_name', 'phone_number',)
    def get_readonly_fields(self, request, obj=None):
        if obj:
            return ('first_name', 'last_name', 'phone_number')
        return ()
    ordering = ('username',)
    list_filter = ('first_name',)
    search_fields = ('username', 'first_name', 'last_name',)
@admin.register(Shop)
class ShopAdmin(admin.ModelAdmin):
    list_display = ('turi', 'name', 'price')
    search_fields = ('name', 'turi')
    actions = (narh,)

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('user', 'shop')
    autocomplete_fields = ('user', 'shop')