from django.test import TestCase
from django.urls import reverse
from phrase_table.models import MyVerb, Pronoun


class TestModel(TestCase):

    def test_create_object(self):
        object = MyVerb.objects.create(english=f"eng", spanish=f"spn")
        self.assertEqual(object.english , "eng")
        self.assertEqual(object.spanish , "spn")
        
    def test_create_object_with_pronoun(self):
        object = Pronoun.objects.create(english=f"eng", spanish=f"spn")
        self.assertEqual(object.english , "eng")
        self.assertEqual(object.spanish , "spn")
        
    def test_create_object_with_pronoun_and_verb(self):
        verb = MyVerb.objects.create(english=f"eng", spanish=f"spn")
        pronoun = Pronoun.objects.create(english=f"eng", spanish=f"spn")
        self.assertEqual(verb.english, "eng")
        self.assertEqual(verb.spanish, "spn")

    def test_create_object_with_pronoun_and_verb2(self):
        pronoun = Pronoun.objects.create(english=f"eng", spanish=f"spn")
        verb = MyVerb.objects.create(english=f"eng", spanish=f"spn")
        self.assertEqual(pronoun.english, "eng")
        self.assertEqual(pronoun.spanish, "spn")
        
    def test_create_multiple_verbs(self):
        MyVerb.objects.create(english=f"eng", spanish=f"spn")
        MyVerb.objects.create(english=f"eng2", spanish=f"spn2")
        self.assertEqual(MyVerb.objects.all().count(),2)
        
    def test_create_multiple_pronouns(self):
        Pronoun.objects.create(english=f"eng", spanish=f"spn")
        Pronoun.objects.create(english=f"eng2", spanish=f"spn2")
        self.assertEqual(Pronoun.objects.all().count(),2)
        
    def test_create_multiple_pronouns_verbs(self):
        MyVerb.objects.create(english=f"eng", spanish=f"spn")
        MyVerb.objects.create(english=f"eng2", spanish=f"spn2")

        Pronoun.objects.create(english=f"eng", spanish=f"spn")
        Pronoun.objects.create(english=f"eng2", spanish=f"spn2")
        self.assertEqual(MyVerb.objects.all().count(),2)
        self.assertEqual(Pronoun.objects.all().count(), 2)

    def test_remove_pronouns_verbs(self):
        item = MyVerb.objects.create(english=f"eng", spanish=f"spn")
        MyVerb.objects.create(english=f"eng2", spanish=f"spn2")
        item.delete()

        item = Pronoun.objects.create(english=f"eng", spanish=f"spn")
        Pronoun.objects.create(english=f"eng2", spanish=f"spn2")
        item.delete()

        self.assertEqual(MyVerb.objects.all().count(), 1)
        self.assertEqual(Pronoun.objects.all().count(), 1)
        
    def test_no_entry(self):
        self.assertEqual(MyVerb.objects.all().count(), 0)
        self.assertEqual(Pronoun.objects.all().count(), 0)

