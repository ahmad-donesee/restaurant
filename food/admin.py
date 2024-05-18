from django.contrib import admin
from .models import Food,CategoryFood
# Register your models here.

@admin.register(CategoryFood)
class CategoryFoodAdmin(admin.ModelAdmin):
    list_display=["name","slug"]
    prepopulated_fields={'slug':('name',)}

@admin.register(Food)
class FoodAdmin(admin.ModelAdmin):
    list_display=["name","price","pub_date"]
    list_filter=["pub_date"]