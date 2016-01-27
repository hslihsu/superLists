from django.core.urlresolvers import reverse
from django.db import models


# Create your models here.
class List(models.Model):
    pass

    def get_absolute_url(self):
        return reverse('lists:viewList', args=(self.id, ))

class Item(models.Model):
    text = models.TextField(default='')
    list = models.ForeignKey(List, default=None)
    
    
    def __str__(self):
        return self.text
    
    
    class Meta:
        ordering = ('id', )
        unique_together = ('list', 'text')