from django.shortcuts import render, get_object_or_404
from rest_framework import generics

# Create your views here.
from ducks.models import Duck
from ducks.serializers import DuckSerializer


class DuckList(generics.ListCreateAPIView):
    queryset = Duck.objects.all()
    serializer_class = DuckSerializer

    def get_object(self):
        queryset = self.get_queryset()
        return get_object_or_404(queryset, pk=self.kwargs['pk'],)
