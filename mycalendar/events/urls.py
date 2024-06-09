# events/urls.py
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import CalendarViewSet, EventViewSet

router = DefaultRouter()
router.register(r'calendars', CalendarViewSet)
router.register(r'events', EventViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
