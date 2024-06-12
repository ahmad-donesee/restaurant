from django.urls import path
from . views import blog_view,detail_view
app_name='blog'

urlpatterns = [
    path('',blog_view,name="blog_view"),
    path('<int:id>/',detail_view,name="detail_view")
]
