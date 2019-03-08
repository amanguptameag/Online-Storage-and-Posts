from django.db import models

class UploadFile(models.Model):
    user = models.CharField(max_length=120, blank=True)
    title = models.CharField(max_length=120, blank=True)
    description = models.CharField(max_length=120, blank=True)
    file = models.FileField(upload_to='files/')
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user

class Share(models.Model):
    user = models.CharField(max_length=120, blank=True)
    title = models.CharField(max_length=120, blank=True)

    def __str__(self):
        return self.user
