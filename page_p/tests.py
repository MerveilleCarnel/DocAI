from django.test import TestCase

from django.test import SimpleTestCase
from django.urls import reverse  # new 
 
class HomepageTests(SimpleTestCase):
    def test_url_exists_at_correct_location(self):
        response = self.client.get("/")
        self.assertEqual(response.status_code, 200)
    def test_url_available_by_name(self):  # new 
        response = self.client.get(reverse("home")) 
        self.assertEqual(response.status_code, 200) 
 
     
class AboutpageTests(SimpleTestCase):
    def test_url_exists_at_correct_location(self):
        response = self.client.get("/about/")
        self.assertEqual(response.status_code, 200)
    def test_url_available_by_name(self):  # new 
        response = self.client.get(reverse("about")) 
        self.assertEqual(response.status_code, 200)      
        
class AboutpageTests(SimpleTestCase):
    def test_url_exists_at_correct_location(self):
        response = self.client.get("/contact/")
        self.assertEqual(response.status_code, 200)   
        
class ChatbotPageTests(SimpleTestCase):
    def test_url_exists_at_correct_location(self):    
        response = self.client.get("/chatbot/")
        self.assertEqual(response.status_code, 200)
    def test_url_available_by_name(self):   
        response = self.client.get(reverse("chatbot")) 
        self.assertEqual(response.status_code, 200) 
 
    def test_template_name_correct(self):  # new 
        response = self.client.get(reverse("chatbot")) 
        self.assertTemplateUsed(response, "chatbot.html")     
        

 
 
 