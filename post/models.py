from django.db import models

# Create A Blog Model
'''
 - pub_date
 - body
 - image
 - user

'''

class Post(models.Model):
    title = models.CharField(max_length=255)
    pub_date = models.DateTimeField()
    body = models.TextField()
    image = models.ImageField(upload_to='images/')
    

# Add the Blog App to the settings

# Create Migration

# Migrate

# Add to the Admin
