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
    year = models.CharField(max_length=50)
    semester =  models.CharField(max_length=100,default=1)
    dateofbirth = models.CharField(max_length=500,default=1)
    admissionno = models.BigIntegerField()
    registerno = models.CharField(max_length=100)
    gen = models.CharField(max_length=100,default=1)
    phoneno = models.BigIntegerField()
    photo = models.CharField(max_length=100)
    emailid = models.CharField(max_length=100)
    housename = models.CharField(max_length=100)
    place = models.CharField(max_length=100)
    postoffice = models.CharField(max_length=100)
    pincode = models.BigIntegerField()
    guardianname = models.CharField(max_length=100)
    phonenumber = models.BigIntegerField()
    LOGIN = models.ForeignKey(login, default=1, on_delete=models.CASCADE)

class subject(models.Model):
    subjectname = models.CharField(max_length=100)
    subjectcode = models.CharField(max_length=100)
    subjectsyllubus = models.CharField(max_length=200)
    semester = models.CharField(max_length=100,default=1)

class sallocation(models.Model):
    STAFF = models.ForeignKey(staff,default=1,on_delete=models.CASCADE)
    semester =  models.CharField(max_length=100,default=1)
    SUBJECT = models.ForeignKey(subject,default=1,on_delete=models.CASCADE)
    year = models.CharField(max_length=50)

class tutorallo(models.Model):
    year = models.CharField(max_length=50)
    STAFF = models.ForeignKey(staff, default=1, on_delete=models.CASCADE)

class attendance(models.Model):
    STUDENT = models.ForeignKey(student,default=1,on_delete=models.CASCADE)
    hour = models.CharField(max_length=20,default=1)
    SALLOCATION = models.ForeignKey(sallocation,default=1,on_delete=models.CASCADE)
    attend = models.CharField(max_length=200,default=1)
    date = models.CharField(max_length=200,default=1)

class mark(models.Model):
    STUDENT = models.ForeignKey(student, default=1, on_delete=models.CASCADE)
    SALLOCATION = models.ForeignKey(sallocation, default=1, on_delete=models.CASCADE)
    semester =  models.CharField(max_length=100,default=1)
    type = models.CharField(max_length=200)
    # SUBJECT = models.ForeignKey(subject, default=1, on_delete=models.CASCADE)
    mark = models.IntegerField()
    grade = models.CharField(max_length=10)

class externalmark(models.Model):
    STUDENT = models.ForeignKey(student, default=1, on_delete=models.CASCADE)
    type = models.CharField(max_length=100, default=1)
    semester = models.CharField(max_length=100, default=1)
    file =  models.CharField(max_length=200)


class parent(models.Model):
    parentname = models.CharField(max_length=100)
    occupation = models.CharField(max_length=100,default=1)
    phoneno = models.BigIntegerField()
    emailid = models.CharField(max_length=200)
    LOGIN = models.ForeignKey(login, default=1, on_delete=models.CASCADE)


class pallocation(models.Model):
    PARENT = models.ForeignKey(parent,default=1,on_delete=models.CASCADE)
    STUDENT = models.ForeignKey(student, default=1, on_delete=models.CASCADE)

class event(models.Model):
    eventname = models.CharField(max_length=200)
    eventdate = models.CharField(max_length=100)
    eventphoto = models.CharField(max_length=300)

class notification(models.Model):
    title = models.CharField(max_length=200)
    discription = models.CharField(max_length=500)
    link = models.CharField(max_length=400,default=1)
    date = models.CharField(max_length=20)

class complaints(models.Model):
    ctitle = models.CharField(max_length=100)
    cdescription = models.CharField(max_length=500)
    cdate = models.CharField(max_length=20)
    creply = models.CharField(max_length=500)
    rdate = models.CharField(max_length=20)
    parid = models.ForeignKey(parent,default=1,on_delete=models.CASCADE)
    stuid = models.ForeignKey(student,default=1,on_delete=models.CASCADE)
    type = models.CharField(max_length=200,default=1)
class material(models.Model):
    title = models.CharField(max_length=100)
    mfile = models.CharField(max_length=200)
    SALLOCATION = models.ForeignKey(sallocation,default=1,on_delete=models.CASCADE)

class additionalinfo(models.Model):
    aadharno = models.CharField(max_length=20)
    bloodg = models.CharField(max_length=20)
    height = models.CharField(max_length=20)
    weight = models.CharField(max_length=20)
    religion = models.CharField(max_length=20)
    caste = models.CharField(max_length=20)
    annincome = models.CharField(max_length=20)
    rationcard = models.CharField(max_length=20)
    skills = models.CharField(max_length=500)
    ten = models.CharField(max_length=20)
    plustwo = models.CharField(max_length=20)
    languages = models.CharField(max_length=50)
    STUDENT = models.ForeignKey(student, default=1, on_delete=models.CASCADE)

class timetable(models.Model):
    day = models.CharField(max_length=100)
    hour = models.CharField(max_length=100)
    SALLOCATION = models.ForeignKey(sallocation, default=1, on_delete=models.CASCADE)







