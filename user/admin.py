from django.contrib import admin
from user.models import UserProfile

# Register your models here.


@admin.register(UserProfile)
class UserProfileAdmon(admin.ModelAdmin):
    list_display = 'id', 'user'
    ordering = '-id',
    # # list_filter = 'created_date',
    search_fields = 'id',
    # list_per_page = 10
    # list_max_show_all = 300
    # list_editable = 'first_name', 'last_name', 'show'
    # list_display_links = 'firstname',
