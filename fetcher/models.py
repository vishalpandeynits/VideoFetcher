from django.db import models

class Video(models.Model):
    video_id = models.CharField(max_length = 15, unique = True)
    title = models.CharField(max_length = 100)
    description = models.CharField(max_length = 5000, null = True, blank = True)
    channel = models.CharField(max_length = 100)
    published_on = models.DateTimeField() # time at which video was published on youtube.
    thumbnail_url = models.URLField()
    created_on = models.DateTimeField(auto_now_add = True) #time at which this instance is recorded in our database.
    last_updated = models.DateTimeField(auto_now = True)

    def __str__(self):
        return f'{self.title}'