from django.db import models

# Create your models here.
class Blogpost1(models.Model):
    post_id1= models.AutoField
    title1 = models.CharField(max_length=50)
    head10 = models.CharField(max_length=500, default="")
    chead10 = models.CharField(max_length=5000, default="")
    head11 = models.CharField(max_length=500, default="")
    chead11 = models.CharField(max_length=5000, default="")
    head12= models.CharField(max_length=500, default="")
    chead12 = models.CharField(max_length=5000, default="")
    pub_date = models.DateField()


    def __str__(self):
        return self.title1