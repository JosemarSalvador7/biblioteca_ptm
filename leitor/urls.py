from django.urls import path
from . import views
urlpatterns = [
    path('leitores/', views.leitores, name='leitores'),
]