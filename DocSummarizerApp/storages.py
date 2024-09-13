
from django.core.files.storage import FileSystemStorage
from django.conf import settings
from django.utils._os import safe_join
import os

class OutsideRootStorage(FileSystemStorage):
    def __init__(self, location=None, base_url=None):
        # Specify your custom location for file storage
        if not location:
            location = os.path.join(settings.BASE_DIR, 'UploadedDocuments')
        super().__init__(location, base_url)

    def path(self, name):
        # Allow saving outside the abase path
        return safe_join(self.location, name)
