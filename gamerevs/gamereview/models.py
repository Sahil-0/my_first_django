from django.db import models
from django.template.defaultfilters import slugify


# Create your models here.
class Tags(models.Model):
    label = models.CharField(max_length=20)

    def __str__(self):
        return self.label


class Game(models.Model):
    title = models.CharField(max_length=100)
    developer = models.CharField(max_length=100)
    platform = models.CharField(max_length=50, default='null')
    label_tag = models.ManyToManyField(Tags)
    slug = models.SlugField(max_length=150, default='null')

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super().save(*args, **kwargs)


class Review(models.Model):
    game = models.ForeignKey(Game, on_delete=models.CASCADE)
    review = models.CharField(max_length=1000)
    date = models.DateField(auto_now=True)
    slug = models.SlugField(max_length=150, default='null')

    def save(self):
        super(Review, self).save()
        self.slug = '%i-%s' % (
            self.id, slugify(self.game.title)
        )
        super(Review, self).save()
