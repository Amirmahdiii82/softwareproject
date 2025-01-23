from django.db import models
from accounts.models import CustomUser

class News(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    likes = models.ManyToManyField(CustomUser, related_name='liked_news')
    
    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return self.title

    def like_count(self):
        return self.likes.count()

    def comment_count(self):
        return self.comments.count()