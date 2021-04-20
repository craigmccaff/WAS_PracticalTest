from django.db import models

class Post(models.Model):
    post_heading = models.CharField(max_length=200)
    pub_date = models.DateTimeField('Date Published')
    post_text = models.CharField(max_length=200)

    def __str__(self):
        return self.post_heading
