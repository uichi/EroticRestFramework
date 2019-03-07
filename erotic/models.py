from django.db import models

class Actresses(models.Model):
    name = models.CharField(max_length=32, unique=True, blank=False, null=False)

    def __str__(self):
        return self.name

class Genres(models.Model):
    name = models.CharField(max_length=32, unique=True, blank=False, null=False)

    def __str__(self):
        return self.name

class Videos(models.Model):
    actress = models.ForeignKey(Actresses, on_delete=models.DO_NOTHING)
    genre = models.ForeignKey(Genres, on_delete=models.DO_NOTHING)
    title = models.CharField(max_length=128, blank=False, null=False)
    description = models.CharField(max_length=516)
    url = models.CharField(max_length=256)

    def __str__(self):
        return self.title