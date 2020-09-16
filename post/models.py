from django.db import models
from django.utils import timezone

# Create your models here.
class Post(models.Model):
    title=models.CharField(max_length=100)
    content=models.TextField(max_length=1000)
    created_at=models.TimeField(default=timezone.now)
    image=models.ImageField(upload_to='post-img/')
    active=models.BooleanField(default=False)




    class Meta:
        verbose_name=("Post")
        verbose_name_plural=("Posts")
    def __str__(self):
        return self.title
    def get_absolute_url(self):
        return reversed("post_detail",kwargs={"pk":self.pk})