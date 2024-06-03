from django.contrib import admin
from .models import Reserve
# Register your models here.
@admin.register(Reserve)
class ReserveAdmin(admin.ModelAdmin):
    list_display = ('name', 'phone', 'email', 'date','time')
    search_fields=('name','email')
    
