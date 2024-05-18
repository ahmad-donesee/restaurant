from django.urls import path
from .views import  fod_cate_item_view  #FoodView,foodlistview

app_name="food"

urlpatterns = [
        path("",fod_cate_item_view,name="foodlist"),
        path("<int:id>/",fod_cate_item_view,name="foodcategory"),
]
