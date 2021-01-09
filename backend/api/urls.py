from .views import apiOverview

from django.urls import path

urlpatterns = [
    path('', apiOverview.as_view() , name="api-overview")
    
]
