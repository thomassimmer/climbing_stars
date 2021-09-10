from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

class Path(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField(max_length=2000)

class Image(models.Model):
    image = models.ImageField(upload_to='images/')
    path = models.ForeignKey(Path, on_delete=models.CASCADE)

class Comment(models.Model):
    path = models.ForeignKey(Path, on_delete=models.CASCADE)
    author = models.CharField(max_length=200)
    note = models.IntegerField(validators=[MaxValueValidator(10), MinValueValidator(0)])
    comment = models.TextField(max_length=2000)