from django.db import models

# Create your models here.
class Event(models.Model):
    title=models.CharField(max_length=255)
    date=models.DateField(auto_now_add=False)
    description=models.TextField()
    image=models.ImageField(upload_to='events/')
    number_images=models.ImageField(upload_to='general/', blank=True,null=True)
    
    def __str__(self):
        return self.title
 
class MomentGallery(models.Model):
    title=models.ForeignKey("web.Event",on_delete=models.CASCADE)
    image=models.ImageField(upload_to='Moment_gallery/')

    class Meta:
        verbose_name_plural="MomentGallery"
        db_table = "Gallery"

    def __str__(self):
        return str( self.id)
