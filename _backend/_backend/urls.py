"""_backend URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from phrase_table.views import VerbViewSet, PronounViewSet
from phrase_table import views
from rest_framework import routers
router = routers.DefaultRouter()
router.register(r"verb", VerbViewSet)
router.register(r"pronoun", PronounViewSet)
urlpatterns = [
    path("", include(router.urls)),
    path("rand_elem/", views.get_random_verb_pair),
    path("en_sent/", views.get_random_english_sentence),
    path("en_es_sent/", views.get_en_es_translation),
    path("en_es_verbs/", views.get_es_right_verb),
    path("en_swa_sent/", views.get_en_swa_translation),
    path("rand_swah_elem/", views.get_random_verb_pair_swa),
    path("en_swa_verbs/", views.get_swa_right_verb)
]
