from django.db import models

# Create your models here.


class Point(models.Model):
    x = models.FloatField()
    y = models.FloatField()

    def __ge__(self, other):
        return self.x >= other.x

class DataFile(models.Model):
    file = models.FileField(blank=False, null=False)

    def get_file_name(self):
        return 'media/'+self.file.name

class ImageFile(models.Model):
    image = models.ImageField(blank=False, null=False, max_length=1000)
    def get_file_name(self):
        return self.image.name

class Distribution(models.Model):
    n = models.IntegerField(blank=False, null=False)
    distribution_type = models.TextField(blank=False, max_length=40)