from django.db import models

# Create your models here.
class urls(models.Model):
    sl_cheat=models.AutoField
    website=models.CharField(max_length=100)
    code=models.CharField(max_length=7,default="")
    

    def __str__(self):
        return (self.website)