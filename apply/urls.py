from django.urls import path
from .views import *

app_name = 'notice'

urlpatterns = [
    path('', ApplyView.as_view()),
    path('del/<int:pk>/', DelApplication.as_view()),
]