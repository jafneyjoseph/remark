from django.db import models

from django.contrib.auth.models import User
class Category(models.Model):
    name = models.CharField(max_length=100)
    image=models.ImageField(upload_to='category',blank=True)

    class Meta:
        ordering=('name',)
        verbose_name='category'
        verbose_name_plural='categories'


    def __str__(self):
        return '{}'.format(self.name)

class Movie(models.Model):
    title = models.CharField(max_length=250)
    desc = models.TextField()
    year = models.IntegerField()
    actors = models.CharField(max_length=250)
    img = models.ImageField(upload_to='gallery')
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    youtube_link = models.URLField(blank=True)

    class Meta:
        ordering = ('title',)
        verbose_name = 'movie'
        verbose_name_plural = 'movies'

    def __str__(self):
        return '{}'.format(self.title)

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    def __str__(self):
        return self.user.username

class Review(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    rating = models.IntegerField()
    comment = models.TextField()


    def __str__(self):
        return f"Review by {self.user.username} for {self.movie.title}"