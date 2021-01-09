from django.db import models

class Branch(models.Model):
    ifsc    = models.CharField(max_length= 100)
    bank_name = models.CharField(max_length=300, blank=True, null= True)
    bank_id = models.CharField(max_length= 100) 
    branch  = models.CharField(max_length= 100)
    address = models.CharField(max_length= 200)
    city    = models.CharField(max_length= 100)
    district= models.CharField(max_length= 100)
    state   = models.CharField(max_length= 100)

    def __str__(self):
        return self.ifsc

    