from django.db import models

# Create your models here.

class login(models.Model):
    username = models.CharField(max_length=200)
    password = models.CharField(max_length=20)
    usertype = models.CharField(max_length=20)

class staff(models.Model):
    staffname = models.CharField(max_length=200)
    photo = models.CharField(max_length=200)
    qualification = models.CharField(max_length=400)
    number = models.BigIntegerField()
    email = models.CharField(max_length=100)
    staffexperiance = models.CharField(max_length=500)
    post = models.CharField(max_length=100)
    LOGIN = models.ForeignKey(login,default=1,on_delete=models.CASCADE)

class student(models.Model):
    studentname = models.CharField(max_length=200)
    year = models.BigIntegerField()
    semester = models.IntegerField()
    dateofbirth = models.BigIntegerField()
    admissionno = models.BigIntegerField()
    registerno = models.CharField(max_length=100)
    phoneno = models.BigIntegerField()
    photo = models.CharField(max_length=100)
    emailid = models.CharField(max_length=100)
    housename = models.CharField(max_length=100)
    place = models.CharField(max_length=100)
    postoffice = models.CharField(max_length=100)
    pincode = models.BigIntegerField()
    guardianname = models.CharField(max_length=100)
    phonenumber = models.BigIntegerField()

class subject(models.Model):
    subjectname = models.CharField(max_length=100)
    subjectcode = models.CharField(max_length=100)
    subjectsyllubus = models.CharField(max_length=200)
    semester = models.IntegerField()

class sallocation(models.Model):
    STAFF = models.ForeignKey(staff,default=1,on_delete=models.CASCADE)
    semester = models.IntegerField()
    SUBJECT = models.ForeignKey(subject,default=1,on_delete=models.CASCADE)

class attendance(models.Model):
    STUDENT = models.ForeignKey(student,default=1,on_delete=models.CASCADE)
    hour = models.IntegerField()
    SUBJECT = models.ForeignKey(subject,default=1,on_delete=models.CASCADE)
    SALLOCATION = models.ForeignKey(sallocation,default=1,on_delete=models.CASCADE)

class mark(models.Model):
    STUDENT = models.ForeignKey(student, default=1, on_delete=models.CASCADE)
    SALLOCATION = models.ForeignKey(sallocation, default=1, on_delete=models.CASCADE)
    semester = models.IntegerField()
    type = models.CharField(max_length=200)
    SUBJECT = models.ForeignKey(subject, default=1, on_delete=models.CASCADE)
    mark = models.IntegerField()
    grade = models.CharField(max_length=10)

class parent(models.Model):
    parentname = models.CharField(max_length=100)
    phoneno = models.BigIntegerField()
    emailid = models.CharField(max_length=200)

class pallocation(models.Model):
    PARENT = models.ForeignKey(parent,default=1,on_delete=models.CASCADE)
    STUDENT = models.ForeignKey(student, default=1, on_delete=models.CASCADE)

class event(models.Model):
    eventname = models.CharField(max_length=200)
    eventdate = models.CharField(max_length=100)
    eventphoto = models.CharField(max_length=300)

class timetable(models.Model):
    day = models.CharField(max_length=100)
    hour = models.CharField(max_length=100)
    subject = models.CharField(max_length=100)
class notification(models.Model):
    title = models.CharField(max_length=200)
    discription = models.CharField(max_length=500)
    date = models.CharField(max_length=20)

class complaints(models.Model):
    ctitle = models.CharField(max_length=100)
    cdescription = models.CharField(max_length=500)
    cdate = models.CharField(max_length=20)
    creply = models.CharField(max_length=500)
    rdate = models.CharField(max_length=20)










