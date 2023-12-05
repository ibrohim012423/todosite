from django.db import models

# Create your models here.
class ish(models.Model):
    nomi = models.CharField(max_length=20)
    matn = models.TextField()
    vaqt = models.DateField(auto_now_add=True)