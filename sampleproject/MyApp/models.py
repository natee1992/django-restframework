from django.db import models

# Create your models here.


class Music(models.Model):
    song = models.TextField()
    singer = models.TextField()
    last_modify_date = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Music"
        verbose_name_plural = "Musics"

    def __str__(self):
        return self.song
