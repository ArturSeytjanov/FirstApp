from django.db import models

# SQL -> 
"""
    CREATE TABLE Post(
        id SERIAL PRIMARY KEY,
        name VARCHAR(20) NOT NULL,
        text TEXT NULL,
        image VARCHAR(20) NULL
    )
"""

# ORM -> 
class Post(models.Model):
    name = models.CharField(max_length=20, null=True, blank=True)
    text = models.TextField()
    image = models.ImageField(upload_to='post/%Y/%m/%d')
    price = models.DecimalField(max_digits=3, decimal_places=2, null=True, blank=True)
    like = models.BooleanField(default=False, null=True, blank=True)

    def __str__(self):
        return self.name 
    









    

