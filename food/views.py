from typing import Any
from django.shortcuts import render,get_object_or_404
from django.views.generic.base import TemplateView
from django.views.generic import ListView

from .models import Food,CategoryFood


def fod_cate_item_view(request,id=None):
    food2=None
    category2=None
    if id:
        category2=CategoryFood.objects.get(id=id)
        food2=Food.objects.filter(category=category2)
    category=CategoryFood.objects.all()
    foods=Food.objects.all()
    context={"food2":food2,"category":category,"foods":foods,"category2":category2}
    return render(request,"food/food.html",context)






# class FoodView(TemplateView):

#     template_name="food/food.html"
    
#     def get_context_data(self, **kwargs):
#         context=super().get_context_data(**kwargs)
#         context['foods']=Food.objects.all()
#         context['category']=CategoryFood.objects.all()
#         return context



# def foodlistview(request,id):
#     category2=CategoryFood.objects.get(id=id)
#     food2=Food.objects.filter(category=category2)
#     category=CategoryFood.objects.all()
#     foods=Food.objects.all()
#     context={"food2":food2,"category":category,"foods":foods}
#     return render(request,"food/food.html",context)

# class FoodView(TemplateView):
#     model=CategoryFood
#     template_name="food/food.html"
#     context_object_name = 'all_categs'

    
#     def get_context_data(self, **kwargs: Any):
#         context=super().get_context_data(**kwargs)
#         context['foods']=Food.objects.all()
#         context['category']=CategoryFood.objects.all()
#         return context
    


# class FoodlistView(ListView):
#     model=CategoryFood
#     def get_queryset(self):
#         self.category = CategoryFood.objects.get(slug=self.kwargs['slug'])
#         queryset = Food.objects.filter(category=self.category)
#         return queryset