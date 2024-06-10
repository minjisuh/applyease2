from rest_framework import generics
from .models import Event, Calendar
from .serializers import EventSerializer, CalendarSerializer

class EventListView(generics.ListCreateAPIView):
    queryset = Event.objects.all()
    serializer_class = EventSerializer

class CalendarListView(generics.ListCreateAPIView):
    queryset = Calendar.objects.all()
    serializer_class = CalendarSerializer
