from rest_framework.generics import ListCreateAPIView
from rest_framework.response import Response
from .serializers import ApplicationSerializer
from .models import Application

# Create your views here.
class ApplyView(ListCreateAPIView):
    serializer_class = ApplicationSerializer
    queryset = Application.objects.all()