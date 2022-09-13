from django.db import models

# Create your models here.
class Note(models.Model):
    note = models.TextField(blank=True, null=True)

    def __str__(self) -> str:
        line_0 = self.note.split('\n')[0]
        if len(line_0 ) > 30:
            return '{}...'.format(line_0[0:30])
        else:
            return line_0