from django.db import models
from django.contrib.auth.models import User


class Drive(models.Model):
    name = models.CharField(max_length=255)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)

    objects = models.Manager()


class Directory(models.Model):
    name = models.CharField(max_length=255)
    drive = models.ForeignKey(Drive, on_delete=models.CASCADE)
    parent_directory = models.ForeignKey('self', null=True, blank=True, on_delete=models.CASCADE)

    objects = models.Manager()


class File(models.Model):
    name = models.CharField(max_length=255)
    drive = models.ForeignKey(Drive, on_delete=models.CASCADE)
    directory = models.ForeignKey(Directory, null=True, blank=True, on_delete=models.CASCADE)

    objects = models.Manager()

    # Ensuring that a file will always be a text file when saved
    def save(self, *args, **kwargs):
        self.is_text_file = True
        super().save(*args, **kwargs)
