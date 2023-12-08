from django.db import models

# Create your models here.
class Students(models.Model):
    name = models.CharField(max_length=20)
    Roll = models.IntegerField(primary_key=True)
    address = models.TextField()
    father_name= models.TextField(default='Rahim')
    
    def __str__(self):
        return f"Roll : {self.Roll} - {self.name}"
    
