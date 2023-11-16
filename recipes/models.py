from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField

STATUS = ((0, "Draft"), (1, "Published"))

class Recipe(models.Model):
    """
    Recipe Model
    """
    name = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="cocktail")
    featured_image = CloudinaryField('image', default='placeholder')
    featured_image_alt = models.CharField(max_length=100, null=False, blank=False, default='green-lime-cocktail')
    serving = models.IntegerField()
    time = models.IntegerField()
    description = models.TextField(blank=False)
    updated_on = models.DateTimeField(auto_now=True)
    ingredients = models.TextField(blank=False)
    directions = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(choices=STATUS, default=0)
    likes = models.ManyToManyField(User, related_name='cocktail_like', blank=True)

    class Meta:
        """
        Displays newest created-on cocktails
        """
        ordering = ["-created_on"]

    def __str__(self):
        return self.name

    def number_of_likes(self):
        """
        Displays total number of likes
        """
        return self.likes.count()
