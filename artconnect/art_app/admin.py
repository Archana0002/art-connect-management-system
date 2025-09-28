from django.contrib import admin
from .models import Artisttable, Usertable, Arttable, Enquirytable  # Ensure correct model names

# Customize EnquiryTable display in Django Admin
@admin.register(Enquirytable)
class EnquiryAdmin(admin.ModelAdmin):
    list_display = ('email', 'phone', 'message', 'submitted_at')  # Display these columns
    
    search_fields = ('email', 'message')  # Enable search by email and message
    readonly_fields = ('submitted_at',)  # Prevent modification of timestamp

# Register other models normally
admin.site.register(Artisttable)
admin.site.register(Usertable)
admin.site.register(Arttable)
