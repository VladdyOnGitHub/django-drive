from django.db import models
from django.contrib.auth.models import User
import uuid


class Drive(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=255)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)

    reader_access = models.ManyToManyField(User, related_name='drives_with_reader_access', blank=True)
    public_access = models.CharField(max_length=20, choices=[('private', 'Private'), ('public', 'Public'),
                                                             ('hidden_public', 'Hidden Public')], default='private')

    objects = models.Manager()

    def rename(self, new_name):
        self.name = new_name
        self.save()

    def add_directory(self, name):
        return self.directories.create(name=name)

    def add_file(self, name, content, directory=None):
        if directory:
            return directory.files.create(name=name, content=content, drive=self)
        else:
            return self.files.create(name=name, content=content)

    def delete_item(self, item_id):
        try:
            item = self.directories.get(id=item_id)
        except Directory.DoesNotExist:
            item = self.files.get(id=item_id)

        item.delete()


class Directory(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=255)
    drive = models.ForeignKey(Drive, related_name='directories', on_delete=models.CASCADE)
    parent_directory = models.ForeignKey('self', null=True, blank=True, related_name='subdirectories', on_delete=models.CASCADE)

    reader_access = models.ManyToManyField(User, related_name='directories_with_reader_access', blank=True)
    public_access = models.CharField(max_length=20, choices=[('private', 'Private'), ('public', 'Public'),
                                                             ('hidden_public', 'Hidden Public')], default='private')
    objects = models.Manager()

    def rename(self, new_name):
        self.name = new_name
        self.save()


class File(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=255)
    drive = models.ForeignKey(Drive, related_name='files', on_delete=models.CASCADE)
    directory = models.ForeignKey(Directory, null=True, blank=True, related_name='files', on_delete=models.CASCADE)

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
