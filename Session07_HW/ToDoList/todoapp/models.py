from django.db import models

import datetime


# Create your models here.

class Post(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    deadline = models.DateField(default=datetime.datetime.now)

    # {{ your_date_variable | timeuntil: target_date }}
    # {{ your_date_variable | timesince: target_date }}
    
    def __str__(self):
        return self.title
    
