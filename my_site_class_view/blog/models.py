from django.db import models
from django.db.models.deletion import SET_NULL

# Create your models here.

class Tag(models.Model):
    caption = models.CharField(max_length=10)

    def __str__(self):
        return f"{self.caption}"

class Author(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField(max_length=100)

    def __str__(self):
        return f"{self.name}"

class Post(models.Model):
    title = models.CharField(max_length=100)
    excerpt = models.CharField(max_length=150)
    image_name = models.ImageField(upload_to="posts", null=True)
    date = models.DateField(auto_now=True)
    slug = models.SlugField(unique=True, db_index=True)
    content = models.TextField()
    author = models.ForeignKey(Author, on_delete=models.SET_NULL, null=True, related_name="posts_author")
    tags = models.ManyToManyField(Tag)

    def __str__(self):
        return f"{self.title} - {self.date}"

class Comment(models.Model):
    user_name = models.CharField(max_length=100)
    user_email = models.EmailField(max_length=100)
    text = models.TextField(max_length=400)
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name = "comments")

    def __str__(self):
        return f"{self.text}"