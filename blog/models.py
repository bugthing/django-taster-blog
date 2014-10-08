from django.db import models
class Posting(models.Model):
    content = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
