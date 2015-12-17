from django.db import models

class List(models.Model):
    pass
    
class Item(models.Model):
    angka = models.IntegerField(default=0)
    tebakan = models.IntegerField(default=0)
    status = models.TextField(default='')
    list = models.ForeignKey(List, default=None)
