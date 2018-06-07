from .models import Duck
from rest_framework import serializers


class DuckSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Duck
        fields = ('id', 'name', 'lastname', 'mail', 'age',)

