from rest_framework.response import Response
from mainApp.models import Resume
from .serializers import ResumeSerializer
from rest_framework.views import APIView
from rest_framework import status

class ResumeView(APIView):
    def post(self, request, format=None):
        serializer = ResumeSerializer(data=request.data )
        if serializer.is_valid():
            serializer.save()
            return Response({'msg':'resume Uploaded Successfully','status':'success','candidate':serializer.data},
            status=status.HTTP_201_CREATED)
        return Response(serializer.errors) 

    def get(self, request, format=None):
        candidates = Resume.objects.all()
        serializer = ResumeSerializer(candidates, many=True)
        return Response({'status':'success', 'candidates':serializer.data}, status=status.HTTP_200_OK)  