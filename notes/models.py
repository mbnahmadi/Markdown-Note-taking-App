from django.db import models
from django.utils.translation import gettext_lazy as _

# Create your models here.

class Notes(models.Model):
    title = models.CharField(max_length=255, verbose_name=_('title'))
    markdown_file = models.FileField(verbose_name=_('file'), upload_to='markdowns/')
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = _('Note')
        verbose_name_plural = _('Notes')

    def __str__(self):
        return f"{self.title}"