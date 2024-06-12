from django.test import TestCase
from .models import Reserve
from .forms import ReservationForm
from .views import reserve


#test reserve model
class TestReservModel(TestCase):
    def setUp(self):
        Reserve.objects.create(name="ahmad",number=4,phone=23)
        Reserve.objects.create(name="ahmad2",number=14,phone=43)
    def test_reserve_model(self):
        name=Reserve.objects.get(id=1)
        name2=Reserve.objects.get(name="ahmad2")
        self.assertEqual(name.number,4)
        self.assertEqual(name2.name,"ahmad2")


# test form  data
class TestReservationForm(TestCase):
    def test_form(self):
        form_data={'name':'ahmad','email':'example@gmail.com','number':'23','phone':'323','date':'2025-3-3','time':'22:12:22'}
        form=ReservationForm(data=form_data)
        self.assertTrue(form.is_valid())
        
#test view

class TestReserveView(TestCase):
    def test_view(self):
        response = self.client.get('/reservation/')
        self.assertEqual(response.status_code, 200)
        
    # def test_redirect(self):
    #     #client=self.Client()
    #     # path='{}?next={}'
    #     form_data={'name':'ahmad','email':'example@gmail.com','number':'23','phone':'323','date':'2025-3-3','time':'22:12:22'}#,'next':reserve('food:foodlist')}
        
    #     response=self.client.post('/reservation/',data=form_data)
    #     self.assertRedirects(response,reserve('food:foodlist'))
        
        