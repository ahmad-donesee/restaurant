from django.urls import path
from .views import  fod_cate_item_view ,menu_view #FoodView,foodlistview

app_name="food"

urlpatterns = [
        path("",fod_cate_item_view,name="foodlist"),
        path("<int:id>/",fod_cate_item_view,name="foodcategory"),
        path("menu/",menu_view,name="menu"),
        path("menu/<int:id>/",menu_view,name="menuitem"),
]
