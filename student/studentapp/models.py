from django.db import models

# Create your models here.
class studentmodel(models.Model):
        firstname = models.CharField(max_length=100)
        lastname = models.CharField(max_length=100)
        currentjob = models.CharField(max_length=100)
        location = models.CharField(max_length=100)
        class Meta:
                db_table="studentinfo"