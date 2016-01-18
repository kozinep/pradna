from django.db import models

class news_Main(models.Model):
    news_date = models.DateField()
    news_text = models.CharField(max_length=50)


