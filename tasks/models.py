from django.db import models

class Task(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)  
    date = models.DateField()
    time = models.TimeField()
    google_event_id = models.CharField(max_length=255, blank=True, null=True)


    def __str__(self):
        return self.title