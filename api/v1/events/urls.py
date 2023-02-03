from django.urls import path
from api.v1.events import views


urlpatterns = [
    path('', views.event),
    path('<int:pk>', views.individual_event),
]