from rest_framework.generics import CreateAPIView
from rest_framework.response import Response
from .serializers import ApplicationSerializer

# Create your views here.
class ApplyView(CreateAPIView):
    serializer_class = ApplicationSerializer