from django.db import models
from django.contrib.auth.models import User
import uuid


class Drive(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=255)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)

    objects = models.Manager()

    def rename(self, new_name):
        self.name = new_name
        self.save()


class Directory(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=255)
    drive = models.ForeignKey(Drive, on_delete=models.CASCADE)
    parent_directory = models.ForeignKey('self', null=True, blank=True, on_delete=models.CASCADE)

    objects = models.Manager()

    def rename(self, new_name):
        self.name = new_name
        self.save()


class File(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=255)
    drive = models.ForeignKey(Drive, on_delete=models.CASCADE)
    directory = models.ForeignKey(Directory, null=True, blank=True, on_delete=models.CASCADE)

    content = models.TextField(default="")

    objects = models.Manager()

    # Ensuring that a file will always be a text file when saved
    def save(self, *args, **kwargs):
        self.is_text_file = True
        super().save(*args, **kwargs)

    def rename(self, new_name):
        self.name = new_name
        self.save()

    def edit_content(self, new_content):
        self.content = new_content
        self.save()
