from django.http import JsonResponse
from django.shortcuts import render
import random

# Create your views here.
from django.shortcuts import render
from phrase_table.models import MyVerb, Pronoun
from phrase_table.serializer import VerbSerializer, PronounSerializer

from rest_framework import viewsets
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAuthenticated

from backend_scripts.converters.english import EnglishConverter
from backend_scripts.utils import exc_to_dict
import logging
logger = logging.getLogger('django')

class VerbViewSet(viewsets.ModelViewSet):
    queryset = MyVerb.objects.all()
    serializer_class = VerbSerializer
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]


class PronounViewSet(viewsets.ModelViewSet):
    queryset = Pronoun.objects.all()
    serializer_class = PronounSerializer
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]
 
 
def get_random_verb_pair(request):
    items = list(MyVerb.objects.all())
    if len(items) > 0:
        random_item = random.choice(items)

        return JsonResponse({'en': random_item.english, 'sp': random_item.spanish})
    return JsonResponse({'en': 'Null', 'sp': 'Null'})


def get_random_english_sentence(request):
    with open("data/test_english_sentences.tsv", "r") as f:
        en_feats = f.read().splitlines()
    en_feats = [feats.strip().split("\t")[0] for feats in en_feats]
    past_tense_exc = exc_to_dict("data/past_tense_exceptions.csv")
    past_part_exc = exc_to_dict("data/irregular_verbs_past_participle.csv")

    english_converter = EnglishConverter(past_tense_exc, past_part_exc)

    random.shuffle(en_feats)
    rand_en_sentence = english_converter.generate_sentence(en_feats[0])
    return JsonResponse({'en':rand_en_sentence})

def get_en_es_translation(request):
    # Provide random sentence with proper translation.
    # call random english sentence to get other incorrect translations
    return JsonResponse({'en': 'I will jump', 'sp': 'yo voluntad saltar'.split(" ")})

def get_es_right_verb(request):
    # provide verb tense
    return JsonResponse({'sentence': 'he ____',
                         'verb': 'jump',
                         'correct': 'jumped' ,
                         'wrong': ['will run', 'eats', 'laughs']
                         })
