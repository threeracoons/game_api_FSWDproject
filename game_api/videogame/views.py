#_____________________________________ change 1

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import VideoGame
from .serializers import VideoGameSerializer

class VideoGameDetails(APIView):
    def get(self, request, title):
        try:
            videogame = VideoGame.objects.get(title=title)
            serializer = VideoGameSerializer(videogame)
            return Response(serializer.data)
        except VideoGame.DoesNotExist:
            return Response({"message": "Video game not found"}, status=status.HTTP_404_NOT_FOUND)

#_______________________________________change 2

# from rest_framework.views import APIView
# from rest_framework.response import Response
# from rest_framework import status
# from .models import VideoGame
# from .serializers import VideoGameSerializer

# class VideoGameList(APIView):
#     def get(self, request):
#         videogames = VideoGame.objects.all()
#         serializer = VideoGameSerializer(videogames, many=True)
#         return Response(serializer.data)

#     def post(self, request):
#         serializer = VideoGameSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)