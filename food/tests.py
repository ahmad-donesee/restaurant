from django.test import TestCase
from .models import CategoryFood,Food
from django.urls import reverse, resolve

from.views import fod_cate_item_view

#---test CategoryFood model----:

class categoryModelTest(TestCase):
    def setUp(self):
        CategoryFood.objects.create(name="meat",slug="meat_2")
        CategoryFood.objects.create(name="meat_1")
    
    def test_cate_model(self):
        cate1=CategoryFood.objects.get(name="meat_1")
        cate=CategoryFood.objects.get(id=1)
        
        self.assertEqual(cate.name,"meat")
        self.assertEqual(cate.slug,"meat_2")
        
        self.assertEqual(cate1.name,"meat_1")


#---test Food model----:

class FoodModelTest(TestCase):
    def setUp(self):
        category_1=CategoryFood.objects.create(name="meat",slug="meat_2")
        category_2=CategoryFood.objects.create(name="meat_3",slug="meat_3")
        
        
        Food.objects.create(category=category_1,name="food_1",price=23,discription="this is good",rate=10,time="2024-3-3 22:22",pub_date="2024-4-4 11:11")
        Food.objects.create(category=category_2,name="food_2",price=25,discription="is nice",rate=15,time="2022-3-3 12:12",pub_date="2025-4-4 11:11")
    
    def test_food_model(self):
        food=Food.objects.get(id=1)
        food1=Food.objects.get(price=25)
        self.assertEqual((food.name,food.price),("food_1",23))
        self.assertEqual(food1.price,25)


#---test url---

class TestView(TestCase):
    def test_fod_cate_item_view(self):
        path=self.client.get("/food/")
        self.assertEqual(path.status_code,200)
        path=self.client.get("/food/", kwargs={"id": 1})
        self.assertEqual(path.status_code,200)
        

