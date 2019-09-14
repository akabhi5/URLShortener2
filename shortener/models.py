from django.db import models

class Urls(models.Model):
    fake_url = models.CharField(max_length=50)
    original_url = models.TextField()

    def __str__(self):
        return self.fake_url
