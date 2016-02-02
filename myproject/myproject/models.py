from django.db import models

class news_Main(models.Model):
    news_date = models.DateField()
    news_text = models.CharField(max_length=50)

class carousel_Main(models.Model):
    carousel_image = models.ImageField(upload_to='static/images')
    carousel_alt = models.TextField(max_length=20)

