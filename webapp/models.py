from django.db import models

# Create your models here.

class GOOD(models.Model):
    GoodID = models.IntegerField(null=False, primary_key=True)
    GoodName = models.CharField(null=False, max_length=20, default='  ')
    GoodPrice = models.IntegerField(null=False)
    GoodPrice1=models.IntegerField(null=False)
    GoodPrice2=models.IntegerField(null=False)
    GoodImage=models.ImageField(null=False )
    def __str__(self):
        return self.GoodName
