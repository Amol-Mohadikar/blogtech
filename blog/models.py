from django.db import models
from django.utils import timezone

# Create your models here.
class Blogpost(models.Model):
    post_id = models.AutoField(primary_key=True,editable=True)
    newpost_id = models.IntegerField(default=6,max_length=100)
    genre=models.CharField(max_length=50,default='no genre')
    tilte = models.CharField(max_length=50,default='no title')
    subtitle = models.CharField(max_length=500, default="")
    pub_date=models.DateField(default=timezone.now())
    thumbnail= models.ImageField(upload_to='blog/images',default='')
    thumbnail2= models.ImageField(upload_to='blog/images',default='')
    thumbnail3= models.ImageField(upload_to='blog/images',default='')
    maintitle1 = models.CharField(max_length=50,default='no title')
    maintitle2 = models.CharField(max_length=50,default='no title')
    maintitle3 = models.CharField(max_length=50,default='no title')
    paragraph1 = models.CharField(max_length=5000, default="")
    paragraph2 = models.CharField(max_length=5000, default="")
    paragraph3 = models.CharField(max_length=5000, default="")
    made_by = models.CharField(max_length=25,default="Blogtech Admin")
    about = models.CharField(max_length=1000,default="Hey Readers! Welcome to Blogtech. for more such Awesome blogs click on next blog. If you love the blog Please like , Comment and Share.")
          
    

    def __str__(self):
        return self.tilte


class Mainblogpost(models.Model):
    post_id = models.AutoField(primary_key= True)
    
    pub_date=models.DateField(default=timezone.now())
    
    maintitle1 = models.CharField(max_length=50,default='no title')
    maintitle2 = models.CharField(max_length=50,default='no title')
    maintitle3 = models.CharField(max_length=50,default='no title')
    paragraph1 = models.CharField(max_length=5000, default="")
    paragraph2 = models.CharField(max_length=5000, default="")
    paragraph3 = models.CharField(max_length=5000, default="")
    made_by = models.CharField(max_length=25,default="Blogtech Admin")
    thumbnail= models.ImageField(upload_to='blog/images',default='')
    thumbnail2= models.ImageField(upload_to='blog/images',default='')
    thumbnail3= models.ImageField(upload_to='blog/images',default='')
    

    def __str__(self):
        return self.maintitle1


class Message(models.Model):
    
    first_name = models.CharField(blank=False,max_length=40)
    last_name=models.CharField(max_length=50,blank=False)
    email = models.EmailField(max_length=80,blank=False)
    contactno = models.IntegerField(max_length=18,blank=False)
    message=models.CharField(max_length=1000,blank=False)
    

    def __str__(self):
        return self.first_name


