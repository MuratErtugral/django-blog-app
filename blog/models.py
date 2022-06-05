from django.db import models
from django.contrib.auth.models import User


class Category(models.Model):
    name= models.CharField(max_length=50)

    def __str__(self):
        return self.name
        
class Post(models.Model):
    poster = models.ForeignKey(User, on_delete=models.PROTECT,null=True, blank=True, editable=False)
    title = models.CharField(max_length=50)
    content = models.TextField()
    image = models.ImageField(upload_to="media/", blank=True, default= "media/4.jpg")
    publish_date = models.DateTimeField(auto_now_add=True)
    last_updated = models.DateTimeField(auto_now=True)
    STATUS_CHOICES=(
        ("1",'published'), 
        ("2",'draft'), 
        ("3",'pending')
        )
    status = models.CharField(max_length=50, choices=STATUS_CHOICES)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.title

    @property
    def num_likes(self):
        return self.liked.all().count()

LIKE_CHOICES = (
    ('Like', 'Like'),
    ('Unlike', 'Unlike'),
    )

class Like(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post =  models.ForeignKey(Post, on_delete=models.CASCADE)
    value = models.CharField(choices=LIKE_CHOICES,default="Like", max_length=10)
class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE,blank=True, null=True)
    post =  models.ForeignKey(Post, on_delete=models.CASCADE,blank=True, null=True)
    comment = models.TextField(blank=True, null=True)





