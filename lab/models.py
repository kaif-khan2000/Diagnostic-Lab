from django.db import models

# Create your models here.

class Application(models.Model):
    sno = models.AutoField(primary_key=True)
    lab_no = models.IntegerField()
    name = models.CharField(max_length=80)
    age = models.IntegerField(default = 0)
    sex = models.CharField(max_length=10)
    recieved_on = models.DateField(auto_now=True)
    ref_by = models.CharField(max_length=50,default = "Dr.Self")
    cost = models.IntegerField(default=0)
    checked = models.BooleanField(default = False)
    
    def __str__(self):
        return f"{self.name} ({self.lab_no})"

class Profile(models.Model):
    sno = models.AutoField(primary_key=True)
    name = models.CharField(max_length = 50,unique=True)

    def __str__(self):
        return self.name

class Test(models.Model):
    sno = models.AutoField(primary_key=True)
    test = models.CharField(max_length=50,unique=True)
    price = models.IntegerField(default = 0)
    range1 = models.CharField(max_length=50,default = "")
    profile = models.ForeignKey(Profile,on_delete=models.CASCADE)    

    def __str__(self):
        return self.test + "(Rs."+str(self.price)+")"
class Value(models.Model):
    primary = 4102000
    lab_no = models.IntegerField(default = 0)

    def __str__(self):
        return "LabNo"
    

class Record(models.Model):
    lab_no = models.IntegerField()
    application = models.ForeignKey(Application,on_delete=models.CASCADE)
    test = models.CharField(max_length=70)
    finding = models.CharField(default="",max_length=30)
    ref = models.CharField(default="",max_length=30)
    note = models.CharField(default="",max_length=100)
    device = models.CharField(default="",max_length=200)
    price = models.IntegerField(default = 0)
    def __str__(self):
        return self.test + "(" + str(self.lab_no) +")"


class Device(models.Model):
    sno = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200,unique=True)

class new(models.Model):
    sno = models.CharField(default=0, max_length=20)