from rest_framework.generics import ListCreateAPIView, DestroyAPIView
from rest_framework.response import Response
from .serializers import ApplicationSerializer
from .models import Application
from rest_framework import status

# Create your views here.
class ApplyView(ListCreateAPIView):
    """
    지원서 작성 / 조회
    """
    serializer_class = ApplicationSerializer
    queryset = Application.objects.all()
    def post(self, request, *args, **kwargs):
        response = super().post(request, *args, **kwargs)
        res = {
            "msg" : "지원서 등록 성공",
            "data" : response.data
        }
        return Response(res, status = status.HTTP_201_CREATED)
    
    def list(self, request, *args, **kwargs):
        response = super().list(request, *args, **kwargs)
        res = {
            "msg" : "지원서 목록 조회 성공",
            "data" : response.data
        }
        return Response(res, status = status.HTTP_200_OK)

class DelApplication(DestroyAPIView):
    queryset = Application.objects.all()
    def delete(self, request, pk, *args, **kwargs):
        apply = ApplicationSerializer(Application.objects.get(pk = pk))
        response = super().delete(request, *args, **kwargs)
        res = {
            "msg" : "지원서 삭제 성공",
            "data" : apply.data
        }
        return Response(res, status=status.HTTP_204_NO_CONTENT)