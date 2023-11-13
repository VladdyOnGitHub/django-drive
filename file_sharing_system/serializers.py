from rest_framework import serializers

from .models import Directory, Drive, File


class DriveSerializer(serializers.ModelSerializer):
    class Meta:
        model = Drive
        fields = "__all__"


class DirectorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Directory
        fields = "__all__"


class FileSerializer(serializers.ModelSerializer):
    class Meta:
        model = File
        fields = "__all__"
