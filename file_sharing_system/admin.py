from django.contrib import admin
from .models import Drive, Directory, File


# Not allowing the user to change whether a file is a text file or not
class FileAdmin(admin.ModelAdmin):
    exclude = ('is_text_file', )


admin.site.register(Drive)
admin.site.register(Directory)
admin.site.register(File, FileAdmin)
