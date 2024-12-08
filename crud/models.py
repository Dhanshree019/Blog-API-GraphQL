from django.db import models

class Post(models.Model):
    title = models.TextField()
    description = models.TextField() 
    author = models.TextField()
    published_date = models.DateTimeField(auto_now_add=True)  
    updated_at = models.DateTimeField(auto_now=True)   

    def __str__(self):
        return self.title

class Comment(models.Model):
    post = models.ForeignKey(Post, related_name='comments', on_delete=models.CASCADE)
    text = models.TextField()
    author = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Comment by {self.author} on {self.post.title}"
