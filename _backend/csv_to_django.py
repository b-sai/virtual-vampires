import django
import os
import sys
import django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "_backend.settings")
django.setup()

from phrase_table.models import MyVerb, Pronoun


with open('../data/verbs.txt', newline='') as f:
    lines = f.read().split("\r\n")
print(lines)

for line in lines:
    tokens = line.split(",")
    eng = tokens[0]
    spn = tokens[1]
    swh = token[2]
    item = MyVerb(english= eng, spanish = sp, swahili=swh)
    item.save()
