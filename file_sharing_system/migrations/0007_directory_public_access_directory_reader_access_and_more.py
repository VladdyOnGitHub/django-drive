# Generated by Django 4.2.7 on 2023-11-11 13:07

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('file_sharing_system', '0006_file_content'),
    ]

    operations = [
        migrations.AddField(
            model_name='directory',
            name='public_access',
            field=models.CharField(choices=[('private', 'Private'), ('public', 'Public'), ('hidden_public', 'Hidden Public')], default='private', max_length=20),
        ),
        migrations.AddField(
            model_name='directory',
            name='reader_access',
            field=models.ManyToManyField(blank=True, related_name='directories_with_reader_access', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='drive',
            name='public_access',
            field=models.CharField(choices=[('private', 'Private'), ('public', 'Public'), ('hidden_public', 'Hidden Public')], default='private', max_length=20),
        ),
        migrations.AddField(
            model_name='drive',
            name='reader_access',
            field=models.ManyToManyField(blank=True, related_name='drives_with_reader_access', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='directory',
            name='drive',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='directories', to='file_sharing_system.drive'),
        ),
        migrations.AlterField(
            model_name='directory',
            name='parent_directory',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='subdirectories', to='file_sharing_system.directory'),
        ),
        migrations.AlterField(
            model_name='file',
            name='directory',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='files', to='file_sharing_system.directory'),
        ),
        migrations.AlterField(
            model_name='file',
            name='drive',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='files', to='file_sharing_system.drive'),
        ),
    ]
