from django.db import models

# Create your models here.
class Mymodel(models.Model):
        employeeName = models.CharField(max_length=100)
        username = models.CharField(max_length=100)
        password = models.CharField(max_length=100)
        emailId = models.CharField(max_length=100)
        phoneNo = models.CharField(max_length=12)
        class Meta:
                db_table="employee"
            
class Newuser(models.Model):
        username = models.CharField(max_length=100)
        password = models.CharField(max_length=100)
        class Meta:
                db_table="admin"

class leave(models.Model):
        employeeName = models.CharField(max_length=100)
        StartDate = models.DateField(max_length=25)
        EndDate = models.DateField(max_length=25)
        LeaveDay = models.CharField(max_length=100)
        class Meta:
                db_table="applyleave"

class worktime(models.Model):
        employeeName = models.CharField(max_length=100)
        clockIn = models.DateTimeField(max_length=50)
        clockOut = models.DateTimeField(max_length=50)
        class Meta:
                db_table="WorkTime"
