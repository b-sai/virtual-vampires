from django.http import JsonResponse
from django.shortcuts import render
import random
import pandas as pd
# Create your views here.
from django.shortcuts import render
from phrase_table.models import MyVerb, Pronoun
from phrase_table.serializer import VerbSerializer, PronounSerializer

from rest_framework import viewsets
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAuthenticated

from backend_scripts.converters.english import EnglishConverter
from backend_scripts.converters.swahili import SwahiliConverter
from backend_scripts.utils import exc_to_dict
import logging
logger = logging.getLogger('django')
sp = ["1s", "2s", "3s", "1p", "2p", "3p"]
tense = ["PAST", "FUT", "IMP", "PRES"]
neg = ["NEG+", ""]
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

        return JsonResponse({'en': random_item.english, 'foreign': random_item.spanish})
    return JsonResponse({'en': 'Null', 'foreign': 'Null'})

def get_random_verb_pair_swa(request):
    with open("data/dict.tsv", "r") as f:
        word_dict = f.read().splitlines()
    en_swa = [words.strip().split("\t")[:2] for words in word_dict]
    random_word = random.choice(en_swa)
    return JsonResponse({'en': random_word[1], 'foreign': random_word[0]}) 


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
    en_word, es_word = get_random_word_pair("en", "foreign")
    feats, rand_sentence = get_random_sentence(en_word)
    rand_sentence_translated = translate(es_word,feats,  "en", "sp")

    return JsonResponse({'en': rand_sentence, 'foreign': rand_sentence_translated.split(" ")}, json_dumps_params={'ensure_ascii': False})

def get_en_swa_translation(request):
    en_word, swa_word = get_random_word_pair_swa("en", "foreign")
    feats, rand_sentence = get_random_sentence(en_word)
    swahili_feats = feats.replace(en_word, swa_word)
    print("A")
    swahili_translation = translate_swahili(swahili_feats)
    swahili_0 = swahili_translation[:len(swahili_translation)//3]
    swahili_1 = swahili_translation[len(swahili_translation)//3:2*len(swahili_translation)//3]
    swahili_2 = swahili_translation[2*len(swahili_translation)//3:]
    return JsonResponse({'en':rand_sentence, 'foreign':[swahili_0, swahili_1, swahili_2]})

def get_es_right_verb(request):
    # provide verb tense
    df = pd.read_csv("data/verbs.tsv", header = None, encoding="utf-8")
    print(df)
    es_words = random.sample(list(df.iloc[:,1]), 4)
    es_word = es_words[0]
    # en_word, es_word = get_random_word_pair("en", "es")
    feats = get_feats(es_word, sp, tense, neg)

    print(es_word)
    feat_str = translate(es_word, feats, "en", "sp")
    # feat_str = "test"
    if " " in feat_str:
        sentence_part = feat_str[:feat_str.rindex(" ")]
        correct_verb = feat_str[feat_str.rindex(" ")+1:]
    else:
        sentence_part = ""
        correct_verb = feat_str
        
    return JsonResponse({'sentence': sentence_part + " __________",
                         'verb': es_word,
                         'correct': correct_verb ,
                         'wrong': es_words[1:]},
                         json_dumps_params={'ensure_ascii': False})

def get_swa_right_verb(request):
    # provide verb tense
    with open("data/dict.tsv", "r") as f:
        word_dict = f.read().splitlines()
    swa_words = [words.strip().split("\t")[0] for words in word_dict]
    swa_word = random.choice(swa_words)
    # en_word, es_word = get_random_word_pair("en", "es")
    feats = []
    swahili_translations = []
    while(1):
        feat = get_feats(swa_word, sp, tense + ["PERF"], neg)
        if(feat not in feats):
            feats = feats + [feat]
            swahili_translations = swahili_translations + [translate_swahili(feat)]
        if(len(feats) == 4):
            break
    #feats = get_feats(swa_word, sp, tense + ["PERF"], neg)
    return JsonResponse({'sentence': feats[0].replace("+"+swa_word, ""),
                         'verb': swa_word,
                         'correct': swahili_translations[0] ,
                         'wrong': swahili_translations[1:]},
                         json_dumps_params={'ensure_ascii': False})
def get_random_word_pair(src, tgt):
    with open("data/verbs.tsv", "r", encoding="utf-8") as f:
        verbs = f.read().splitlines()
    verbs = [verb.split(",") for verb in verbs]
    
    res = random.choice(verbs)
    return res[0], res[1]


def get_random_word_pair_swa(src, tgt):
    with open("data/dict.tsv", "r") as f:
        word_dict = f.read().splitlines()
    en_swa = [words.strip().split("\t")[:2] for words in word_dict]
    random_word = random.choice(en_swa)
    return random_word[1], random_word[0]

def get_random_sentence(word):
    
    past_tense_exc = exc_to_dict("data/past_tense_exceptions.csv")
    past_part_exc = exc_to_dict("data/irregular_verbs_past_participle.csv")

    english_converter = EnglishConverter(past_tense_exc, past_part_exc)
    feats = get_feats(word, sp, tense, neg)
    sentence = english_converter.generate_sentence(feats)
    
    return feats, sentence

def get_feats(word, sp, tense, neg):
    feats = random.choice(neg)  + random.choice(sp) + "+" + random.choice(tense) + "+" + word
    return feats

def translate(word, feats, src, tgt):
    """
    word: word to translate in target lang
    feats: features of the word (incuding word)
    """
    feats = feats[:feats.rindex("+")]+ "+" + word
    df = pd.read_csv("data/test_spanish_sentences.tsv", sep="\t", header = None, encoding="utf-8")
    df = df[df[0] == feats]
    
    return df[1].values[0]

def translate_swahili(feats):
    irregular_exc = exc_to_dict("data/irregular_verbs_swahili.csv")
    
    swahili_converter = SwahiliConverter(irregular_exc)
    return swahili_converter.generate_sentence(feats)

    
