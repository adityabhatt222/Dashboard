from django.db import models

class Post(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to='post_images/', null=True, blank=True)
    likes = models.PositiveIntegerField(default=0)
    shares = models.PositiveIntegerField(default=0)
    
    def __str__(self):
        return self.title 

    def like(self):
        self.likes += 1
        self.save()

    def share(self):
        self.shares += 1
        self.save()
