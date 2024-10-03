from django.test import TestCase
from django.urls import reverse

class CustomAccountTests(TestCase):
    def test_url_exists_at_correct_location_login_view(self):
        response = self.client.get('/accounts/login/')
        self.assertEqual(response.status_code, 200)
    
    def test_login_view_name(self):
        response = self.client.get(reverse('login'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'registration/login.html')
        
