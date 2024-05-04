#______________________________ change 1

# from rest_framework import serializers
# from .models import VideoGame

# class VideoGameSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = VideoGame
#         fields = ['title', 'platform', 'genre', 'release_date', 'price']



#_____________________________ change 2

from rest_framework import serializers
from .models import VideoGame

class VideoGameSerializer(serializers.ModelSerializer):
    class Meta:
        model = VideoGame
        fields = ['title', 'platform', 'genre', 'release_date', 'price']
