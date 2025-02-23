from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()  

# Create your models here.
class Article(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField(blank = True,null = True, default = True)
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE, null = True)

    def __str__(self):
        return self.title


class Comment(models.Model):
    article = models.ForeignKey('Article', on_delete=models.CASCADE, null=True, blank=True)
    content = models.TextField(blank = True,null = True, default = True)
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE, null = True)
    
    def __str__(self):
        return f"Comment on {self.post.title}"
