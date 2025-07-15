from django.db import models

# Create your models here.

class Blog(models.Model):
    TYPES={
        "Journal": 'Journal',
        "Life updates": 'Live updates',
        "Travel":'Travel',
        "Personal development":'Personal development',
        "IT":'IT'
    }
    title = models.CharField(max_length=200)
    content = models.TextField()
    image = models.ImageField(upload_to='blog_images',blank=True,null=True)
    type=models.CharField(max_length=50,choices= TYPES,default="Journal")
    created_at = models.DateTimeField(auto_now_add=True)
    published_at = models.BooleanField(default=True)
    def __str__(self):
        return self.title
