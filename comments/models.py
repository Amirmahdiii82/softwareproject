from django.db import models
from accounts.models import CustomUser
from news.models import News

class Comment(models.Model):
    news = models.ForeignKey(News, on_delete=models.CASCADE, related_name='comments')
    author = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    parent = models.ForeignKey('self', null=True, blank=True, on_delete=models.CASCADE, related_name='replies')

    def __str__(self):
        return f'Comment by {self.author.username} on {self.news.title}'