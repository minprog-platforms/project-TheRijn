from django.contrib import admin
from .models import Listing, Category, Bid, User
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin


admin.site.register(Listing)
admin.site.register(Category)
admin.site.register(Bid)


@admin.register(User)
class UserAdmin(BaseUserAdmin):
    pass
