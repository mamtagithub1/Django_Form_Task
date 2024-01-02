from django.db import models  
class Employee(models.Model):  
    eid = models.CharField(max_length=20)  
    ename = models.CharField(max_length=100)  
    eemail = models.EmailField()  
    econtact = models.CharField(max_length=15)  
    class Meta:  
        db_table = "employee" 

class Video(models.Model):
    caption=models.CharField(max_length=190)
    video=models.FileField(upload_to="video/%y")
    def __str__(self):
        return self.caption
