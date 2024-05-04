#__________________________________________________ change 1

# from django.db import models

# class VideoGame(models.Model):
#     title = models.CharField(max_length=100)
#     platform = models.CharField(max_length=50)
#     genre = models.CharField(max_length=50)
#     release_date = models.DateField()
#     price = models.DecimalField(max_digits=8, decimal_places=2)

#     def __str__(self):
#         return self.title

#____________________________________________________ change 2

# models.py
from django.db import models

class VideoGame(models.Model):
    title = models.CharField(max_length=100)
    platform = models.CharField(max_length=50)
    genre = models.CharField(max_length=50)
    release_date = models.DateField()
    price = models.DecimalField(max_digits=8, decimal_places=2)

    def __str__(self):
        return self.title
