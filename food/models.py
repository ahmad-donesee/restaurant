from django.db import models

# Create your models here.
class CategoryFood(models.Model):
    name=models.CharField(max_length=30)
    slug=models.SlugField(unique=True)
    
    def __str__(self):
        return self.name
    class Meta:
        verbose_name_plural="  دسته بندی غدا "

class Food(models.Model):
    category=models.ForeignKey(CategoryFood,related_name="category",on_delete=models.CASCADE)
    name=models.CharField(max_length=30)
    image=models.ImageField(upload_to="image/food/%Y/%m/%d/")
    price=models.PositiveIntegerField()
    discription=models.TextField()
    rate=models.IntegerField()
    time=models.DateTimeField()
    pub_date=models.DateTimeField()
    
    def __str__(self):
        return self.name
    class Meta:
        ordering=['-pub_date']
        verbose_name_plural="غذا"


class SuggestionForm(models.Model):
    name=models.CharField(max_length=30,blank=True,null=True)
    email=models.EmailField(blank=True,null=True)
    content=models.TextField(blank=True,null=True)
    
    def __str__(self):
        return self.name
    class Meta:
        verbose_name_plural=" پیشنهادات  "