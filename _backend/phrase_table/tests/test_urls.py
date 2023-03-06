from django.test import TestCase
from django.urls import reverse
from phrase_table.models import MyVerb, Pronoun
class TestUrls(TestCase):
    
    def test_view_returns_OK(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)

    def test_rand_elem_view_returns_OK(self):
        MyVerb.objects.create(
            english=f"eng", spanish=f"spn")

        response = self.client.get('/rand_elem/')
        print(response)
        self.assertEqual(response.status_code, 200)


