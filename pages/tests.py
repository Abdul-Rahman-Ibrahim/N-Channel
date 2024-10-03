from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse
from .models import News

class NewsTest(TestCase):
    # @classmethod
    # def setUpTestData(cls) -> None:
    #     cls.user = get_user_model().objects.create_user(
    #         username='testuser', email='testuser@gmail.com', password='secret'
    #     )

    #     cls.post = News.objects.create(
            
    #     )


    def test_url_exist_home(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
    
    def test_home_page_view(self):
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'home.html')
    
    def test_admin_page_view(self):
        response = self.client.get(reverse('admins_home'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'admins_home.html')