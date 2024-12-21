from django.contrib import admin
from .models import Quota

class QuotaAdmin(admin.ModelAdmin):
    list_display = ('user', 'total_time', 'limit', 'can_process', 'reset_quota')
    search_fields = ('user__email',)
    list_filter = ('user',)

    def can_process(self, obj):
        # Display whether the user can process more time
        return obj.can_process(1)  # Pass a small value to check if the limit is not exceeded
    can_process.boolean = True  # Show a checkbox for boolean fields

    def reset_quota(self, obj):
        # Display a button to reset quota in the admin interface
        return f"Reset quota for {obj.user.email}"

    reset_quota.short_description = "Reset Quota"

admin.site.register(Quota, QuotaAdmin)
