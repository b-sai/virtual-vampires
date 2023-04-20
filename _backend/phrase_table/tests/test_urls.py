from django.test import TestCase
from django.urls import reverse
from phrase_table.models import MyVerb, Pronoun
from ast import literal_eval
class TestUrls(TestCase):
    
    def test_view_returns_OK(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)

    def test_rand_elem_view_returns_OK(self):
        MyVerb.objects.create(
            english=f"eng", spanish=f"spn")

        response = self.client.get('/rand_elem/')
        self.assertEqual(response.status_code, 200)

    def test_rand_elem_view_returns_json(self):
        MyVerb.objects.create(
            english=f"eng", spanish=f"spn")

        response = self.client.get('/rand_elem/')
        self.assertEqual(literal_eval(response.content.decode("utf-8")), {'en': 'eng', 'foreign': 'spn'})

    def test_rand_elem_view_returns_OK_no_entries(self):

        response = self.client.get('/rand_elem/')

        self.assertEqual(response.status_code, 200)
        
    def test_rand_elem_view_returns_json_no_entries(self):
    
        response = self.client.get('/rand_elem/')
        self.assertEqual(literal_eval(response.content.decode(
            "utf-8")), {'en': 'Null', 'foreign': 'Null'})

