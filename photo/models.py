from django.db import models
from imagekit.models import ProcessedImageField
from imagekit.processors import ResizeToFill
# Create your models here.
class Photo(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    #image = models.ImageField(blank=True)
    image = ProcessedImageField(
                upload_to = "photo/image",
                processors = [ResizeToFill(150,150)],
                format = 'JPEG',
                options = {"quality":90}
        )
    
    def __str__(self):
        return self.title
        
class Comment(models.Model):
    photo = models.ForeignKey(Photo, on_delete=models.CASCADE)
    content = models.CharField(max_length=50)
    
    def __str__(self):
        return self.content