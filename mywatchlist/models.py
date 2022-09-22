from django.db import models

class MyWatchList(models.Model):
    watched = models.TextField()
    title = models.CharField(max_length=255)
    rating = models.DecimalField(max_digits=5, decimal_places=1)
    release_date = models.TextField()
    review = models.TextField()
