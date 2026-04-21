from django.db import models

class Post(models.Model):
    post_id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=200)
    content = models.TextField()
    author_name = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)

class Comment(models.Model):
    post_id = models.ForeignKey(Post, on_delete=models.CASCADE,related_name='comments')
    author_name = models.CharField(max_length=200)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)