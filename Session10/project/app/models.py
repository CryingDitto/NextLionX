from django.db import models

class Post(models.Model):
    title = models.CharField(max_length=50)
    content = models.TextField()

    def __str__(self):
        return self.title

class Comment(models.Model):
    # Post에서 참조할 때 ForeignKey 받아옴
    post = models.ForeignKey(Post, on_delete = models.CASCADE, related_name = 'comments')
    content = models.TextField()

    def __str__(self):
        return self.content

class Example(models.Model):
    title = models.CharField(max_length = 50)
    content = models.TextField()
    date = models.DateTimeField()
    blank_field = models.CharField(max_length = 50, null=True, blank=True)
