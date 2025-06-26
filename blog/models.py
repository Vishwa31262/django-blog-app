from django.db import models

class Post(models.Model):
    title = models.CharField(max_length=200)  # Blog title
    body = models.TextField()                # Blog content
    created_at = models.DateTimeField(auto_now_add=True)  # Date of post

    def __str__(self):
        return self.title