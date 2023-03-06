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

    random_item = random.choice(items)
    return JsonResponse({'en': random_item.english, 'sp': random_item.spanish})