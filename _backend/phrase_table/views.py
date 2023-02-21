from django.http import JsonResponse
from django.shortcuts import render
import random

# Create your views here.
from django.shortcuts import render
from .models import MyVerb, Pronoun
from .serializer import VerbSerializer, PronounSerializer

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
    num_entries = MyVerb.objects.count()
    rand_id = random.randint(0, num_entries-1)
    item = MyVerb.objects.get(id = rand_id)
    return JsonResponse({'en': item.english, 'sp': item.spanish})