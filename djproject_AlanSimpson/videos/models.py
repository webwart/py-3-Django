from django.db import models
from django.urls import reverse

# Create your models here.

class Video(models.Model):
    CATEGORY_CHOICES = [
        (1, 'HTML/CSS'),
        (2, 'JavaScript'),
        (3, 'Python'),
        (4, 'Django'),
        (5, 'Salsa'),
        (6, 'RKW')
    ]

    SKILL_LEVEL_CHOICES = [
        (1, 'Beginner'),
        (2, 'Intermediate'),
        (3, 'Advanced'),
    ]

# 'ytube_vi_URL', 'ytube_pl_ID', 'ytube_pl_URL'

    title = models.CharField("title",max_length=128)
    author = models.CharField("author", max_length=64)
    description = models.TextField(blank=True, null=True)
    youtube_vid = models.CharField("yoTu Video ID", max_length=11 , default="8BDH3ceqKOM")
    ytube_vi_URL = models.CharField("yoTu Video URL",max_length=128, null=True)
    ytube_pl_ID = models.CharField("yoTu playlist ID",max_length=33 , null=True)
    ytube_pl_URL = models.CharField("yoTu playlist URL",max_length=128 , null=True)
    stars_count = models.DecimalField(max_digits=2, decimal_places=1)
    category_id = models.IntegerField(choices = CATEGORY_CHOICES)
    skill_level_id = models.IntegerField(choices = SKILL_LEVEL_CHOICES)
    is_active = models.BooleanField(default=True)
    date_posted = models.DateTimeField(auto_now_add=True)
    last_updated = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["-stars_count","title"]

    def __str__(self):
        return self.title + ' (' + self.author + ')'

    def get_absolute_url(self):
        return reverse('allpages-home')