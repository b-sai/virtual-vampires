# from msilib.schema import Verb
from rest_framework import serializers
from phrase_table.models import MyVerb, Pronoun


class VerbSerializer(serializers.ModelSerializer):
    class Meta:
        model = MyVerb
        fields = '__all__'


class PronounSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pronoun
        fields = '__all__'


class TableSerializer(serializers.Serializer):
    verb = VerbSerializer(many=True)
    pronoun = PronounSerializer(many=True)
