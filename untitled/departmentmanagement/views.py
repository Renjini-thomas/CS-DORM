import datetime
import random

from django.core.files.storage import FileSystemStorage
from django.db.models import Q
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from departmentmanagement.models import *
# Create your views here.

systempath = r"D:\Final  backup\CS DORM (cs dept managmt system)\untitled\departmentmanagement\static\file\\"

def logins(request):
    return render(request,"index.html")
def loginsbutton(request):
    un = request.POST['textfield']
    pw = request.POST['textfield2']

    obj = login.objects.filter(username=un,password=pw)
    if obj.exists():
        obj = obj[0]
        request.session['lin'] ="1"
        if obj.usertype == 'admin':
            return HttpResponse("<script>alert('welcome to home page');window.location='/adminhomepage'</script>")
        elif obj.usertype =='STAFF':
            request.session['sid'] = staff.objects.get(LOGIN=obj.id).id
            return HttpResponse("<script>alert('welcome to home page');window.location='/STAFFhomepage'</script>")

    else:
        return HttpResponse("<script>alert('invalid username or password');window.location='/'</script>")
def logout(request):
    request.session['lin'] = "0"
    return HttpResponse("<script>alert('logout successfully');window.location='/'</script>")




def chaangepassword(request):
    if request.session['lin'] == "0":
        return HttpResponse("<script>alert('your session has expired.please login again');window.location='/'</script>")

    return render(request,"admin/CHANGE PASSWORD.html")
def chaangepasswordbutton(request):
    if request.session['lin'] == "0":
        return HttpResponse("<script>alert('your session has expired.please login again');window.location='/'</script>")
    pw = request.POST['textfield']
    np = request.POST['textfield2']
    cp = request.POST['textfield3']
    if np == cp:
        data = login.objects.filter(password=pw,usertype='admin')
        if data.exists():
            data.update(password=np)
            return HttpResponse("<script>alert('password updated successfully');window.location='/'</script>")
        else:
            return HttpResponse("<script>alert('invalid details');window.location='/chaangepassword'</script>")
    else:
        return HttpResponse("<script>alert('password not valid');window.location='/chaangepassword'</script>")



def replymanagement(request,id):
    if request.session['lin'] == "0":
        return HttpResponse("<script>alert('your session has expired.please login again');window.location='/'</script>")
    return render(request,"admin/REPLY MANAGEMENT.html",{"id":id})

def replymanagementbutton(request,id):
    if request.session['lin'] == "0":
        return HttpResponse("<script>alert('your session has expired.please login again');window.location='/'</script>")
    repl = request.POST['textarea']

    robj = complaints.objects.get(id = id)
    robj.creply = repl
    robj.rdate = datetime.datetime.now().strftime("%Y-%m-%d")
    robj.save()
    return HttpResponse("<script>alert('Added successfully');window.location='/viewcomplaints'</script>")


def eventmanagement(request):
    if request.session['lin'] == "0":
        return HttpResponse("<script>alert('your session has expired.please login again');window.location='/'</script>")
    return render(request,"admin/EVENT MANAGEMENT.html")
def eventmanagementbutton(request):
    if request.session['lin'] == "0":
        return HttpResponse("<script>alert('your session has expired.please login again');window.location='/'</script>")
    en = request.POST['textfield']
    ep = request.FILES['fileField']
    ed = request.POST['textfield2']
    fs = FileSystemStorage()
    d = datetime.datetime.now().strftime("%Y%m%d%H%M%S")
    fs.save(systempath+d+'.jpg',ep)
    eobj = event()
    eobj.eventname = en
    eobj.eventdate = ed
    eobj.eventphoto = '/static/file/'+d+'.jpg'
    eobj.save()
    print(en, ep, ed)
    return HttpResponse("<script>alert('Added successfully');window.location='/eventmanagement'</script>")

def notificationmanagement(request):
    if request.session['lin'] == "0":
        return HttpResponse("<script>alert('your session has expired.please login again');window.location='/'</script>")
    return render(request,"admin/NOTIFICATION MANAGEMENT.html")
def notificationmanagementbutton(request):
    if request.session['lin'] == "0":
        return HttpResponse("<script>alert('your session has expired.please login again');window.location='/'</script>")
    tit = request.POST['textfield']
    dis = request.POST['textarea']
    link = request.POST['textfield3']
    nobj = notification()
    nobj.title = tit
    nobj.discription = dis
    nobj.date = datetime.datetime.now().date()
    nobj.link = link
    nobj.save()
    return HttpResponse("<script>alert('Added successfully');window.location='/notificationmanagement'</script>")


def parentallocation(request,i):
    if request.session['lin'] == "0":
        return HttpResponse("<script>alert('your session has expired.please login again');window.location='/'</script>")
    p = parent.objects.all()
    s = student.objects.all()
    request.session['sid'] = i
    return render(request,"admin/PARENT ALLOCATION.html",{"p":p,"s":s,"ij":i})

def parentallocationbutton(request,i,p):
    if request.session['lin'] == "0":
        return HttpResponse("<script>alert('your session has expired.please login again');window.location='/'</script>")
    pob1 = pallocation()
    pob1.PARENT_id = p
    pob1.STUDENT_id = i
    pob1.save()
    return HttpResponse("<script>alert('Added successfully');window.location='/viewpallocation/"+str(request.session['sid'])+"'</script>")

def parentmanagement(request):
    if request.session['lin'] == "0":
        return HttpResponse("<script>alert('your session has expired.please login again');window.location='/'</script>")
    return render(request,"admin/PARENT MANAGEMENT.html")
def parentmanagementbutton(request):
    if request.session['lin'] == "0":
        return HttpResponse("<script>alert('your session has expired.please login again');window.location='/'</script>")
    pn = request.POST['textfield']
    po = request.POST['textfield5']
    pp = request.POST['textfield2']
    pe = request.POST['textfield3']
    if login.objects.filter(username=pe).exists():
        return HttpResponse("<script>alert('Already Existed');window.location='/parentmanagement'</script>")
    aobj = login()
    aobj.username = pe
    aobj.password = random.randint(0000,9999)
    aobj.usertype = 'parent'
    aobj.save()
    paobj = parent()
    paobj.parentname = pn
    paobj.occupation = po
    paobj.phoneno = pp
    paobj.emailid = pe
    paobj.LOGIN=aobj
    paobj.save()
    return HttpResponse("<script>alert('Added successfully');window.location='/parentmanagement'</script>")


def staffmanagement(request):
    if request.session['lin'] == "0":
        return HttpResponse("<script>alert('your session has expired.please login again');window.location='/'</script>")
    return render(request,"admin/STAFF MANAGEMENT.html")
def staffmanagementbutton(request):
    if request.session['lin'] == "0":
        return HttpResponse("<script>alert('your session has expired.please login again');window.location='/'</script>")
    sn = request.POST['textfield']
    sp = request.FILES['file']
    sq = request.POST['textarea']
    sno = request.POST['textfield2']
    sem = request.POST['textfield3']
    sex = request.POST['textarea2']
    spst = request.POST['textfield4']
    fs = FileSystemStorage()
    d = datetime.datetime.now().strftime("%y%m%d%H%M%S")
    fs.save(systempath+d+'.jpg',sp)
    if login.objects.filter(username=sem).exists():
        return HttpResponse("<script>alert('Already Existed');window.location='/staffmanagement'</script>")

    lobj = login()
    lobj.username = sem
    lobj.password = random.randint(0000,9999)
    lobj.usertype = 'STAFF'
    lobj.save()
    sobj = staff()
    sobj.staffname = sn
    sobj.photo = '/static/file/'+d+'.jpg'
    sobj.qualification = sq
    sobj.number = sno
    sobj.email = sem
    sobj.staffexperiance = sex
    sobj.post = spst
    sobj.LOGIN=lobj
    sobj.save()
    return HttpResponse("<script>alert('Added successfully');window.location='/staffmanagement'</script>")

def studentmanagement(request):
    if request.session['lin'] == "0":
        return HttpResponse("<script>alert('your session has expired.please login again');window.location='/'</script>")
    year = []
    for i in range(2021,int(datetime.datetime.now().year)+1):
        year.append(
            str(i) + '-' + str(int(i)+3)
        )

    return render(request,"admin/STUDENT MANAGEMENT.html",{"x":year})
def studentmanagementbutton(request):
    if request.session['lin'] == "0":
        return HttpResponse("<script>alert('your session has expired.please login again');window.location='/'</script>")
    sn = request.POST['textfield']
    sy = request.POST['textfield2']
    ssem = request.POST['textfield14']
    sdob = request.POST['textfield6']
    adn = request.POST['textfield3']
    regn = request.POST['textfield4']
    gen = request.POST['textfield19']
    phn = request.POST['textfield5']
    sp = request.FILES['fileField']
    se = request.POST['textfield7']
    sh = request.POST['textfield8']
    spl = request.POST['textfield9']
    spost = request.POST['textfield10']
    spin = request.POST['textfield11']
    sgn = request.POST['textfield12']
    sgph = request.POST['textfield13']
    fs = FileSystemStorage()
    d = datetime.datetime.now().strftime("%y%m%d%H%M%S")
    fs.save(systempath + d + '.jpg', sp)
    if login.objects.filter(username=se).exists():
        return HttpResponse("<script>alert('Already Existed');window.location='/staffmanagement'</script>")
    lobj = login()
    lobj.username = se
    lobj.password = random.randint(0000,9999)
    lobj.usertype = 'student'
    lobj.save()
    sob1 = student()
    sob1.studentname = sn
    sob1.year = sy
    sob1.semester = ssem
    sob1.dateofbirth = sdob
    sob1.admissionno = adn
    sob1.registerno = regn
    sob1.gen = gen
    sob1.phoneno = phn
    sob1.photo = '/static/file/'+d+'.jpg'
    sob1.emailid = se
    sob1.housename = sh
    sob1.place = spl
    sob1.postoffice = spost
    sob1.pincode = spin
    sob1.guardianname = sgn
    sob1.phonenumber = sgph
    sob1.LOGIN=lobj
    sob1.save()
    return HttpResponse("<script>alert('Added successfully');window.location='/studentmanagement'</script>")

def viewattendence(request):
    if request.session['lin'] == "0":
        return HttpResponse("<script>alert('your session has expired.please login again');window.location='/'</script>")
    year = []
    for i in range(2021, int(datetime.datetime.now().year) + 1):
        year.append(
            str(i) + '-' + str(int(i) + 3)
        )
    return render(request,"admin/VIEW ATTENDENCE.html",{"x":year})
def searchattend(request):
    if request.session['lin'] == "0":
        return HttpResponse("<script>alert('your session has expired.please login again');window.location='/'</script>")
    ye = request.POST['select']
    sem = request.POST['select1']
    data = attendance.objects.filter(STUDENT__semester=sem,STUDENT__year=ye)
    year = []
    for i in range(2021, int(datetime.datetime.now().year) + 1):
        year.append(
            str(i) + '-' + str(int(i) + 3)
        )
    return render(request, "admin/VIEW ATTENDENCE.html", {"x":year,"data":data})

def viewmark(request):
    if request.session['lin'] == "0":
        return HttpResponse("<script>alert('your session has expired.please login again');window.location='/'</script>")
    year = []
    for i in range(2021, int(datetime.datetime.now().year) + 1):
        year.append(


            str(i) + '-' + str(int(i) + 3)
        )
    return render(request,"admin/VIEW MARK.html",{"x":year})
def searchmark(request):
    if request.session['lin'] == "0":
        return HttpResponse("<script>alert('your session has expired.please login again');window.location='/'</script>")
    ye = request.POST['select']
    sem = request.POST['select1']
    data = mark.objects.filter(STUDENT__semester=sem,STUDENT__year=ye)
    year = []
    for i in range(2021, int(datetime.datetime.now().year) + 1):
        year.append(
            str(i) + '-' + str(int(i) + 3)
        )
    return render(request, "admin/VIEW MARK.html", {"x":year,"data":data})

def searchrecord(request):
    year = []
    for i in range(2021, int(datetime.datetime.now().year) + 1):
        year.append(
            str(i) + '-' + str(int(i) + 3)
        )
    return render(request, "admin/search.html",{"y":year})



def searchpost(request):
    year = []
    for i in range(2021, int(datetime.datetime.now().year) + 1):
        year.append(
            str(i) + '-' + str(int(i) + 3)
        )
    data = student.objects.filter(year=request.POST['textfield2']).order_by('semester', 'studentname')
    return render(request, "admin/search.html",{"y":year,"data":data})

def searchpostallo(request):
    year = []
    for i in range(2021, int(datetime.datetime.now().year) + 1):
        year.append(
            str(i) + '-' + str(int(i) + 3)
        )
    data2 = sallocation.objects.filter(year=request.POST['textfield3'])
    return render(request, "admin/search.html",{"y":year,"data2":data2})

def searchmore(request,id):
    if request.session['lin'] == "0":
        return HttpResponse("<script>alert('your session has expired.please login again');window.location='/'</script>")

    try:
        data = additionalinfo.objects.get(STUDENT=id)
        data2 = externalmark.objects.filter(STUDENT=id)
        # print(data.rationcard)
        return render(request, "admin/VIEWMOREDETAILSadmin.html",{"data":data,"data2":data2})
    except Exception as e:
        print(e,"jjj")
        return render(request, "admin/VIEWMOREDETAILSadmin.html",{"data2":data2})


def subjectallocation(request):
    if request.session['lin'] == "0":
        return HttpResponse("<script>alert('your session has expired.please login again');window.location='/'</script>")

    s = subject.objects.all()
    st = staff.objects.all()
    year = []
    for i in range(2021, int(datetime.datetime.now().year) + 1):
        year.append(
            str(i) + '-' + str(int(i) + 3)
        )
    return render(request,"admin/SUBJECT ALLOCATION.html",{"s":s,"st":st,"x":year})

def subjectallocationbutton(request):
    if request.session['lin'] == "0":
        return HttpResponse("<script>alert('your session has expired.please login again');window.location='/'</script>")
    ss = request.POST['select']
    ssem = request.POST['textfield']
    ssub = request.POST['select2']
    syear = request.POST['textfield2']
    if sallocation.objects.filter(STAFF_id = ss,semester = ssem,SUBJECT_id = ssub,year = syear).exists():
        return HttpResponse("<script>alert('Already Added');window.location='/subjectallocation#log'</script>")

    sob2 = sallocation()
    sob2.STAFF_id = ss
    sob2.semester = ssem
    sob2.SUBJECT_id = ssub
    sob2.year = syear
    sob2.save()
    return HttpResponse("<script>alert('Added successfully');window.location='/subjectallocation'</script>")

def subjectmanagement(request):
    if request.session['lin'] == "0":
        return HttpResponse("<script>alert('your session has expired.please login again');window.location='/'</script>")
    return render(request,"admin/SUBJECT MANAGEMENT.html")
def subjectmanagementbutton(request):
    if request.session['lin'] == "0":
        return HttpResponse("<script>alert('your session has expired.please login again');window.location='/'</script>")
    sn = request.POST['textfield']
    sc = request.POST['textfield2']
    ss = request.FILES['fileField']
    sem = request.POST['textfield3']
    fs = FileSystemStorage()
    d = datetime.datetime.now().strftime("%y%m%d%H%M%S")
    fs.save(systempath + d + '.pdf', ss)
    smobj = subject()
    smobj.subjectname = sn
    smobj.subjectcode = sc
    smobj.subjectsyllubus = '/static/file/'+d+'.pdf'
    smobj.semester = sem
    smobj.save()
    return HttpResponse("<script>alert('Added successfully');window.location='/subjectmanagement'</script>")

def tutorallocation(request):
    if request.session['lin'] == "0":
        return HttpResponse("<script>alert('your session has expired.please login again');window.location='/'</script>")
    st = staff.objects.all()
    year = []
    for i in range(2021, int(datetime.datetime.now().year) + 1):
        year.append(
            str(i) + '-' + str(int(i) + 3)
        )

    return render(request, "admin/TUTORALLO.html",{"x":year,"st":st})

def tutorallobutton(request):
    yr = request.POST['select']
    staff = request.POST['select2']
    if tutorallo.objects.filter(year = yr,STAFF_id = staff).exists():
        return HttpResponse("<script>alert('Already added');window.location='/tutorallocation'</script>")
    obj = tutorallo()
    obj.year = yr
    obj.STAFF_id = staff
    obj.save()
    return HttpResponse("<script>alert('Added successfully');window.location='/tutorallocation'</script>")

def viewtutorallo(request):
    if request.session['lin'] == "0":
        return HttpResponse("<script>alert('your session has expired.please login again');window.location='/'</script>")
    data = tutorallo.objects.all()
    print(data,"hhhhhhh")
    return render(request,"admin/VIEWTUTORALLO.html",{"data":data})

def deletetutoralloc(request,i):
    if request.session['lin'] == "0":
        return HttpResponse("<script>alert('your session has expired.please login again');window.location='/'</script>")
    id = i
    tutorallo.objects.get(id=id).delete()
    return HttpResponse("<script>alert('Deleted successfully');window.location='/viewtutorallo#log'</script>")




def timetablemanagement(request):
    if request.session['lin'] == "0":
        return HttpResponse("<script>alert('your session has expired.please login again');window.location='/'</script>")
    t=sallocation.objects.all()
    return render(request,"admin/TIME TABLE MANAGEMENT.html",{"t":t})
def timetablemanagementbutton(request):
    if request.session['lin'] == "0":
        return HttpResponse("<script>alert('your session has expired.please login again');window.location='/'</script>")

    day = request.POST['select']
    hr = request.POST['textfield2']
    sub = request.POST['select2']
    if timetable.objects.filter(day = day,hour = hr,SALLOCATION_id = sub).exists():
        return HttpResponse("<script>alert('Already exists');window.location='/timetablemanagement#log'</script>")
    tobj = timetable()
    tobj.day = day
    tobj.hour = hr
    tobj.SALLOCATION_id = sub
    tobj.save()
    return HttpResponse("<script>alert('Added successfully');window.location='/timetablemanagement'</script>")

def viewcomplaints(request):
    if request.session['lin'] == "0":
        return HttpResponse("<script>alert('your session has expired.please login again');window.location='/'</script>")
    data = complaints.objects.all()
    return render(request,"admin/VIEW COMPLAINTS.html",{"data":data})

def viewevents(request):
    if request.session['lin'] == "0":
        return HttpResponse("<script>alert('your session has expired.please login again');window.location='/'</script>")
    data = event.objects.all()
    return render(request,"admin/VIEW EVENT.html",{"data":data})



def viewnotification(request):
    if request.session['lin'] == "0":
        return HttpResponse("<script>alert('your session has expired.please login again');window.location='/'</script>")
    data = notification.objects.all()
    return render(request,"admin/VIEW NOTIFICATION.html",{"data":data})

def viewpallocation(request,i):
    if request.session['lin'] == "0":
        return HttpResponse("<script>alert('your session has expired.please login again');window.location='/'</script>")
    data = pallocation.objects.filter(STUDENT=i)
    return render(request,"admin/VIEW PARENT ALLOCATION.html",{"data":data})

def viewparent(request):
    if request.session['lin'] == "0":
        return HttpResponse("<script>alert('your session has expired.please login again');window.location='/'</script>")
    data = parent.objects.all()
    return render(request,"admin/VIEW PARENT.html",{"data":data})

def viewstaff(request):
    if request.session['lin'] == "0":
        return HttpResponse("<script>alert('your session has expired.please login again');window.location='/'</script>")
    data = staff.objects.all()
    for data2 in data:
        q = tutorallo.objects.filter(STAFF=data2.id)
        if q.exists():
            data2.inc = q[0].year
        else:
            data2.inc = 'There is no allocation'
    return render(request,"admin/VIEW STAFF.html",{"data":data})

def viewstudent(request):
    if request.session['lin'] == "0":
        return HttpResponse("<script>alert('your session has expired.please login again');window.location='/'</script>")
    data = student.objects.all().order_by('semester', 'studentname')
    year = []
    for i in range(2021, int(datetime.datetime.now().year) + 1):
        year.append(
            str(i) + '-' + str(int(i) + 3)
        )
    return render(request,"admin/VIEW STUDENT.html",{"data":data,"y":year})



def viewstudent_post(request):
    if request.session['lin'] == "0":
        return HttpResponse("<script>alert('your session has expired.please login again');window.location='/'</script>")
    data = student.objects.filter(year=request.POST['textfield2']).order_by('semester', 'studentname')
    year = []
    for i in range(2021, int(datetime.datetime.now().year) + 1):
        year.append(
            str(i) + '-' + str(int(i) + 3)
        )
    return render(request,"admin/VIEW STUDENT.html",{"data":data,"y":year})




def viewsubject(request):
    if request.session['lin'] == "0":
        return HttpResponse("<script>alert('your session has expired.please login again');window.location='/'</script>")
    data = subject.objects.all()
    return render(request,"admin/VIEW SUBJECT.html",{"data":data,"y":data})

def viewtimetable(request):
    if request.session['lin'] == "0":
        return HttpResponse("<script>alert('your session has expired.please login again');window.location='/'</script>")
    data = timetable.objects.all()
    return render(request,"admin/VIEW TIME TABLE.html")

def searchsem(request):
    data = timetable.objects.filter(SALLOCATION__semester=request.POST['textfield3'])
    return render(request, "admin/VIEW TIME TABLE.html", {"data": data})


def adminhomepage(request):
    if request.session['lin'] == "0":
        return HttpResponse("<script>alert('your session has expired.please login again');window.location='/'</script>")
    return render(request,"admin/index.html")

def viewsubjectallocation(request):
    if request.session['lin'] == "0":
        return HttpResponse("<script>alert('your session has expired.please login again');window.location='/'</script>")
    data = sallocation.objects.all()
    return render(request,"admin/VIEW SUBJECT ALLOCATION.html",{"data":data})

def deleteevent(request,id):
    if request.session['lin'] == "0":
        return HttpResponse("<script>alert('your session has expired.please login again');window.location='/'</script>")
    event.objects.get(id=id).delete()
    return HttpResponse("<script>alert('Deleted successfully');window.location='/viewevents'</script>")
def deletenotifi(request,id):
    if request.session['lin'] == "0":
        return HttpResponse("<script>alert('your session has expired.please login again');window.location='/'</script>")
    notification.objects.get(id=id).delete()
    return HttpResponse("<script>alert('Deleted successfully');window.location='/viewnotification'</script>")
def deletepallo(request,id):
    if request.session['lin'] == "0":
        return HttpResponse("<script>alert('your session has expired.please login again');window.location='/'</script>")
    pallocation.objects.get(id=id).delete()
    return HttpResponse("<script>alert('Deleted successfully');window.location='/viewpallocation/"+str(request.session['sid'])+"'</script>")

def deleteparent(request,id):
    if request.session['lin'] == "0":
        return HttpResponse("<script>alert('your session has expired.please login again');window.location='/'</script>")
    parent.objects.get(id=id).delete()
    return HttpResponse("<script>alert('Deleted successfully');window.location='/viewparent'</script>")
def deletestaff(request,id):
    if request.session['lin'] == "0":
        return HttpResponse("<script>alert('your session has expired.please login again');window.location='/'</script>")
    staff.objects.get(id = id).delete()
    return HttpResponse("<script>alert('Deleted successfully');window.location='/viewstaff'</script>")
def deletestudent(request,id):
    if request.session['lin'] == "0":
        return HttpResponse("<script>alert('your session has expired.please login again');window.location='/'</script>")
    student.objects.get(id=id).delete()
    return HttpResponse("<script>alert('Deleted successfully');window.location='/viewstudent'</script>")
def deletesub(request,id):
    if request.session['lin'] == "0":
        return HttpResponse("<script>alert('your session has expired.please login again');window.location='/'</script>")
    subject.objects.get(id=id).delete()
    return HttpResponse("<script>alert('Deleted successfully');window.location='/viewsubject'</script>")
def deletesuballo(request,id):
    if request.session['lin'] == "0":
        return HttpResponse("<script>alert('your session has expired.please login again');window.location='/'</script>")
    sallocation.objects.get(id=id).delete()
    return HttpResponse("<script>alert('Deleted successfully');window.location='/viewsubjectallocation'</script>")
def deletetimetable(request,id):
    if request.session['lin'] == "0":
        return HttpResponse("<script>alert('your session has expired.please login again');window.location='/'</script>")
    timetable.objects.get(id=id).delete()
    return HttpResponse("<script>alert('Deleted successfully');window.location='/viewtimetable'</script>")



def editevent(request,id):
    if request.session['lin'] == "0":
        return HttpResponse("<script>alert('your session has expired.please login again');window.location='/'</script>")
    data = event.objects.get(id=id)
    return render(request,"admin/EVENT EDIT.html",{"data":data})
def eventeditbutton(request,id):
    if request.session['lin'] == "0":
        return HttpResponse("<script>alert('your session has expired.please login again');window.location='/'</script>")
    en = request.POST['textfield']
    ed = request.POST['textfield2']
    if 'fileField' in request.FILES:
        ep = request.FILES['fileField']
        fs = FileSystemStorage()
        d = datetime.datetime.now().strftime("%Y%m%d%H%M%S")
        fs.save(systempath+d+'.jpg',ep)
        eobj = event.objects.get(id=id)
        eobj.eventname = en
        eobj.eventdate = ed
        eobj.eventphoto = '/static/file/' + d + '.jpg'
        eobj.save()
    eobj = event.objects.get(id=id)
    eobj.eventname = en
    eobj.eventdate = ed
    eobj.save()

    return HttpResponse("<script>alert('Added successfully');window.location='/viewevents'</script>")

def editnoti(request, id):
    if request.session['lin'] == "0":
        return HttpResponse("<script>alert('your session has expired.please login again');window.location='/'</script>")
    data = notification.objects.get(id=id)
    return render(request, "admin/NOTIFICATION EDIT.html",{"data":data})
def notificationeditbutton(request,id):
    if request.session['lin'] == "0":
        return HttpResponse("<script>alert('your session has expired.please login again');window.location='/'</script>")
    tit = request.POST['textfield']
    dis = request.POST['textarea']
    dat = request.POST['textfield3']
    nobj = notification.objects.get(id=id)
    nobj.title = tit
    nobj.discription = dis
    nobj.link = dat
    nobj.save()
    return HttpResponse("<script>alert('Added successfully');window.location='/viewnotification'</script>")


def editpalloc(request,id):
    if request.session['lin'] == "0":
        return HttpResponse("<script>alert('your session has expired.please login again');window.location='/'</script>")
    data = pallocation.objects.get(id=id)
    return render(request,"admin/PARENT ALLOCAEDIT.html",{"data":data})
def parentallocationeditbutton(request,id):
    if request.session['lin'] == "0":
        return HttpResponse("<script>alert('your session has expired.please login again');window.location='/'</script>")
    par = request.POST['select']
    stu = request.POST['select2']
    pob1 = pallocation.objects.get(id=id)
    pob1.PARENT = par
    pob1.STUDENT = stu
    pob1.save()
    return HttpResponse("<script>alert('Added successfully');window.location='/viewpallocation'</script>")

def editparent(request,id):
    if request.session['lin'] == "0":
        return HttpResponse("<script>alert('your session has expired.please login again');window.location='/'</script>")
    data = parent.objects.get(id=id)
    return render(request,"admin/PARENT MANAGEMENTEDIT.html",{"data":data})
def parentmanagementeditbutton(request,id):
    if request.session['lin'] == "0":
        return HttpResponse("<script>alert('your session has expired.please login again');window.location='/'</script>")
    pn = request.POST['textfield']
    po = request.POST['textfield5']
    pp = request.POST['textfield2']
    pe = request.POST['textfield3']
    paobj = parent.objects.get(id=id)
    paobj.parentname = pn
    paobj.occupation = po
    paobj.phoneno = pp
    paobj.emailid = pe
    paobj.save()
    return HttpResponse("<script>alert('Added successfully');window.location='/viewparent'</script>")



def editstaff(request,id):
    if request.session['lin'] == "0":
        return HttpResponse("<script>alert('your session has expired.please login again');window.location='/'</script>")
    data = staff.objects.get(id=id)
    return render(request,"admin/STAFF MANAGEMENTEDIT.html",{"data":data})
def staffmanagementeditbutton(request,id):
    if request.session['lin'] == "0":
        return HttpResponse("<script>alert('your session has expired.please login again');window.location='/'</script>")
    sn = request.POST['textfield']

    sq = request.POST['textarea']
    sno = request.POST['textfield2']
    sem = request.POST['textfield3']
    sex = request.POST['textarea2']
    spst = request.POST['textfield4']
    fs = FileSystemStorage()
    if 'file' in request.FILES:
        sp = request.FILES['file']
        d = datetime.datetime.now().strftime("%y%m%d%H%M%S")
        fs.save(systempath + d + '.jpg', sp)
        sobj = staff.objects.get(id=id)
        sobj.staffname = sn
        sobj.photo = '/static/file/' + d + '.jpg'
        sobj.qualification = sq
        sobj.number = sno
        sobj.email = sem
        sobj.staffexperiance = sex
        sobj.post = spst
        sobj.save()
    sobj = staff.objects.get(id=id)
    sobj.staffname = sn
    sobj.qualification = sq
    sobj.number = sno
    sobj.email = sem
    sobj.staffexperiance = sex
    sobj.post = spst
    sobj.save()
    return HttpResponse("<script>alert('Added successfully');window.location='/viewstaff'</script>")


def editstud(request,id):
    if request.session['lin'] == "0":
        return HttpResponse("<script>alert('your session has expired.please login again');window.location='/'</script>")
    data = student.objects.get(id=id)
    year = []
    for i in range(2021, int(datetime.datetime.now().year) + 1):
        year.append(
            str(i) + '-' + str(int(i) + 3)
        )

    return render(request,"admin/STUDENT MANAGEMENTEDIT.html",{"x":year,"data":data})


def studentmanagementeditbutton(request,id):
    if request.session['lin'] == "0":
        return HttpResponse("<script>alert('your session has expired.please login again');window.location='/'</script>")
    sn = request.POST['textfield']
    sy = request.POST['textfield2']
    ssem = request.POST['textfield14']
    sdob = request.POST['textfield6']
    adn = request.POST['textfield3']
    regn = request.POST['textfield4']
    gen = request.POST['textfield19']
    phn = request.POST['textfield5']
    se = request.POST['textfield7']
    sh = request.POST['textfield8']
    spl = request.POST['textfield9']
    spost = request.POST['textfield10']
    spin = request.POST['textfield11']
    sgn = request.POST['textfield12']
    sgph = request.POST['textfield13']
    if 'fileField' in request.FILES:
        sp = request.FILES['fileField']
        fs = FileSystemStorage()
        d = datetime.datetime.now().strftime("%y%m%d%H%M%S")
        fs.save(systempath + d + '.jpg', sp)
        sob1 = student.objects.get(id=id)
        sob1.studentname = sn
        sob1.year = sy
        sob1.semester = ssem
        sob1.dateofbirth = sdob
        sob1.admissionno = adn
        sob1.registerno = regn
        sob1.gen = gen
        sob1.phoneno = phn
        sob1.photo = '/static/file/' + d + '.jpg'
        sob1.emailid = se
        sob1.housename = sh
        sob1.place = spl
        sob1.postoffice = spost
        sob1.pincode = spin
        sob1.guardianname = sgn
        sob1.phonenumber = sgph
        sob1.save()

    sob1 = student.objects.get(id=id)
    sob1.studentname = sn
    sob1.year = sy
    sob1.semester = ssem
    sob1.dateofbirth = sdob
    sob1.admissionno = adn
    sob1.registerno = regn
    sob1.gen = gen
    sob1.phoneno = phn
    sob1.emailid = se
    sob1.housename = sh
    sob1.place = spl
    sob1.postoffice = spost
    sob1.pincode = spin
    sob1.guardianname = sgn
    sob1.phonenumber = sgph
    sob1.save()
    return HttpResponse("<script>alert('Added successfully');window.location='/viewstudent'</script>")

def editsuballo(request,id):
    if request.session['lin'] == "0":
        return HttpResponse("<script>alert('your session has expired.please login again');window.location='/'</script>")
    data = sallocation.objects.get(id=id)
    print(data,"da")
    year = []
    for i in range(2021, int(datetime.datetime.now().year) + 1):
        year.append(
            str(i) + '-' + str(int(i) + 3)
        )

    return render(request,"admin/SUBJECT ALLOCATIONEDIT.html",{"data":data,"x":year})

def subjectallocationeditbutton(request,id):
    if request.session['lin'] == "0":
        return HttpResponse("<script>alert('your session has expired.please login again');window.location='/'</script>")
    ss = request.POST['select']
    ssem = request.POST['textfield']
    ssub = request.POST['select2']
    syear = request.POST['textfield2']
    sob2 = sallocation.objects.get(id=id)
    sob2.STAFF = ss
    sob2.semester = ssem
    sob2.SUBJECT = ssub
    sob2.year = syear
    sob2.save()
    return HttpResponse("<script>alert('Added successfully');window.location='/viewsubjectallocation'</script>")

def editsub(request,id):
    if request.session['lin'] == "0":
        return HttpResponse("<script>alert('your session has expired.please login again');window.location='/'</script>")
    data = subject.objects.get(id=id)
    return render(request,"admin/SUBJECT MANAGEMENTEDIT.html",{"data":data})
def subjectmanagementeditbutton(request,id):
    if request.session['lin'] == "0":
        return HttpResponse("<script>alert('your session has expired.please login again');window.location='/'</script>")
    sn = request.POST['textfield']
    sc = request.POST['textfield2']

    sem = request.POST['textfield3']
    if 'fileField' in request.FILES:
        ss = request.FILES['fileField']
        fs = FileSystemStorage()
        d = datetime.datetime.now().strftime("%y%m%d%H%M%S")
        fs.save(systempath + d + '.pdf', ss)
        smobj = subject.objects.get(id=id)
        smobj.subjectname = sn
        smobj.subjectcode = sc
        smobj.subjectsyllubus = '/static/file/' + d + '.pdf'
        smobj.semester = sem
        smobj.save()
    smobj = subject.objects.get(id=id)
    smobj.subjectname = sn
    smobj.subjectcode = sc
    smobj.semester = sem
    smobj.save()
    return HttpResponse("<script>alert('Added successfully');window.location='/viewsubject'</script>")


def edittt(request,id):
    if request.session['lin'] == "0":
        return HttpResponse("<script>alert('your session has expired.please login again');window.location='/'</script>")
    data = timetable.objects.get(id=id)
    return render(request,"admin/TIME TABLE MANAGEMENTEDIT.html",{"data":data})
def timetablemanagementeditbutton(request,id):
    if request.session['lin'] == "0":
        return HttpResponse("<script>alert('your session has expired.please login again');window.location='/'</script>")
    day = request.POST['select']
    hr = request.POST['textfield2']
    sub = request.POST['select2']
    tobj = timetable.objects.get(id=id)
    tobj.day = day
    tobj.hour = hr
    tobj.subject = sub
    tobj.save()
    return HttpResponse("<script>alert('Added successfully');window.location='/viewtimetable'</script>")


#=======================================================================================================================module 2 staff

def inc(request):
    if request.session['lin'] == "0":
        return HttpResponse(
            "<script>alert('your session has expired.please login again');window.location='/'</script>")
    data = student.objects.filter(year=tutorallo.objects.filter(STAFF=request.session['sid'])[0].year).order_by('studentname')
    return render(request, "STAFF/INCHARGE VIEW STUDENT.html", {"data": data})


def incsearch(request):
    if request.session['lin'] == "0":
        return HttpResponse("<script>alert('your session has expired.please login again');window.location='/'</script>")
    data = student.objects.filter(Q(year=tutorallo.objects.filter(STAFF=request.session['sid'])[0].year) & Q(studentname__icontains=request.POST['textfield2'])).order_by('studentname')
    return render(request,"STAFF/INCHARGE VIEW STUDENT.html",{"data":data})


def STAFFhomepage(request):
    if request.session['lin'] == "0":
        return HttpResponse("<script>alert('your session has expired.please login again');window.location='/'</script>")
    t=tutorallo.objects.filter(STAFF=request.session['sid'])
    if t.exists():
        request.session['cinc'] = "1"
    else:
        request.session['cinc'] = "0"

    return render(request,"STAFF/index.html")


def allocacatedsubjects(request):
    if request.session['lin'] == "0":
        return HttpResponse("<script>alert('your session has expired.please login again');window.location='/'</script>")
    data = sallocation.objects.filter(STAFF=request.session['sid'])
    return render(request,"STAFF/ALLOCATED SUBJECTS.html",{"data":data})

def attendencemanagement(request):
    if request.session['lin'] == "0":
        return HttpResponse("<script>alert('your session has expired.please login again');window.location='/'</script>")
    return render(request,"STAFF/ATTENDENCE MANAGEMENT.html")

def markmanagement(request):
    if request.session['lin'] == "0":
        return HttpResponse("<script>alert('your session has expired.please login again');window.location='/'</script>")
    return render(request, "STAFF/MARK MANAGEMENT.html")

def materialmanagement(request,i):
    if request.session['lin'] == "0":
        return HttpResponse("<script>alert('your session has expired.please login again');window.location='/'</script>")
    return render(request, "STAFF/MATERIAL MANAGEMENT.html",{"id":i})
def materialmanagementbutton(request,i):
    if request.session['lin'] == "0":
        return HttpResponse("<script>alert('your session has expired.please login again');window.location='/'</script>")
    tit = request.POST["textfield"]
    file = request.FILES["fileField"]
    fs = FileSystemStorage()
    d = datetime.datetime.now().strftime("%y%m%d%H%M%S")
    fs.save(systempath + d + '.pdf', file)
    ob = material()
    ob.title = tit
    ob.mfile = '/static/file/'+d+'.pdf'
    ob.SALLOCATION_id = i
    ob.save()
    return HttpResponse("<script>alert('Added successfully');window.location='/allocacatedsubjects'</script>")

def viewmaterial(request,i):
    if request.session['lin'] == "0":
        return HttpResponse("<script>alert('your session has expired.please login again');window.location='/'</script>")
    data = material.objects.filter(SALLOCATION=i)
    request.session['aid'] = i
    return render(request, "STAFF/VIEW MATERIAL.html", {"data": data})

def editmaterial(request,i):
    if request.session['lin'] == "0":
        return HttpResponse("<script>alert('your session has expired.please login again');window.location='/'</script>")
    data = material.objects.get(id=i)
    return render(request,"STAFF/MATERIAL MANAGEMENT EDIT.html",{"data":data})
def materialmanagementeditbutton(request,i):
    if request.session['lin'] == "0":
        return HttpResponse("<script>alert('your session has expired.please login again');window.location='/'</script>")
    tit = request.POST["textfield"]
    if 'fileField' in request.FILES:
        file = request.FILES["fileField"]
        fs = FileSystemStorage()
        d = datetime.datetime.now().strftime("%y%m%d%H%M%S")
        fs.save(systempath + d + '.pdf', file)
        ob = material.objects.get(id=i)
        ob.title = tit
        ob.mfile = file
        ob.save()
    ob = material.objects.get(id=i)
    ob.title = tit
    ob.save()
    return HttpResponse("<script>alert('Added successfully');window.location='/allocacatedsubjects'</script>")

def externalmarkuniv(request,id):
    if request.session['lin'] == "0":
        return HttpResponse("<script>alert('your session has expired.please login again');window.location='/'</script>")
    s = student.objects.all()
    return render(request, "STAFF/INDIVIDUALSEMRESULTS.html",{"s":id})

def externalmarkbutton(request,s):
    if request.session['lin'] == "0":
        return HttpResponse("<script>alert('your session has expired.please login again');window.location='/'</script>")
    sem = request.POST["select"]
    type = request.POST["select3"]
    rfile = request.FILES["fileField"]
    fs = FileSystemStorage()
    d = datetime.datetime.now().strftime("%y%m%d%H%M%S")
    fs.save(systempath + d + '.pdf', rfile)
    if externalmark.objects.filter(semester = sem,type = type,STUDENT_id = s).exists():
        return HttpResponse("<script>alert('Added successfully');window.location='/inc#log'</script>")
    if type == 'SEM WISE' or type == 'IMP/SUPPLY':
        ob = externalmark()
        ob.semester = sem
        ob.type = type
        ob.STUDENT_id = s
        ob.file= '/static/file/'+d+'.pdf'
        ob.save()
        return HttpResponse("<script>alert('Added successfully');window.location='/inc#log'</script>")
    else:
        ob = externalmark()
        ob.semester = 'NIL'
        ob.type = type
        ob.STUDENT_id = s
        ob.file = '/static/file/' + d + '.pdf'
        ob.save()
        return HttpResponse("<script>alert('Added successfully');window.location='/inc#log'</script>")

def viewexternal(request,i):
    if request.session['lin'] == "0":
        return HttpResponse("<script>alert('your session has expired.please login again');window.location='/'</script>")
    data = externalmark.objects.filter(STUDENT=i).order_by('-id')
    return render(request,"STAFF/VIEWSEMRESULTS.html",{"data":data})

def deleteexternalmark(request,i):
    if request.session['lin'] == "0":
        return HttpResponse("<script>alert('your session has expired.please login again');window.location='/'</script>")
    externalmark.objects.get(id=i).delete()
    return HttpResponse("<script>alert('Deleted successfully');window.location='/inc#log'</script>")

def moredetails(request,i):
    if request.session['lin'] == "0":
        return HttpResponse("<script>alert('your session has expired.please login again');window.location='/'</script>")
    s = student.objects.all()
    return render(request, "STAFF/MOREDETAILS.html",{"s":i})
def moredetailsbutton(request,s):
    if request.session['lin'] == "0":
        return HttpResponse("<script>alert('your session has expired.please login again');window.location='/'</script>")
    adno = request.POST['textfield']
    bg = request.POST['select3']
    hei = request.POST['textfield3']
    wei = request.POST['textfield4']
    rel = request.POST['select']
    cast = request.POST['select2']
    aain = request.POST['textfield8']
    ration = request.POST['select4']
    skill = request.POST['textarea']
    tenp = request.POST['textfield9']
    pltwop = request.POST['textfield10']
    lang = request.POST['textarea2']
    if additionalinfo.objects.filter(STUDENT=s).exists():
        return HttpResponse("<script>alert('Added successfully');window.location='/inc#log'</script>")
    obj = additionalinfo()
    obj.aadharno = adno
    obj.bloodg = bg
    obj.height = hei
    obj.weight = wei
    obj.religion = rel
    obj.caste = cast
    obj.annincome = aain
    obj.rationcard = ration
    obj.skills = skill
    obj.ten = tenp
    obj.plustwo = pltwop
    obj.languages = lang
    obj.STUDENT_id = s
    obj.save()
    return HttpResponse("<script>alert('Added successfully');window.location='/inc#log'</script>")
def viewmoredetails(request,i):
    if request.session['lin'] == "0":
        return HttpResponse("<script>alert('your session has expired.please login again');window.location='/'</script>")
    try:
        data = additionalinfo.objects.get(STUDENT=i)
        return render(request, "STAFF/VIEWMOREDETAILS.html", {"data": data})
    except Exception as e:
        s = student.objects.get(id = i)
        return HttpResponse("<script>alert('There is no additional info for "+str(s.studentname)+" ');window.location='/inc#log'</script>")

def deletemoredetails(request,i):
    if request.session['lin'] == "0":
        return HttpResponse("<script>alert('your session has expired.please login again');window.location='/'</script>")
    additionalinfo.objects.get(id=i).delete()
#     return HttpResponse("<script>alert('Deleted successfully');window.location='/viewmoredetails/"+str(request.session['aid'])+"'</script>")
#
# def editmoredetails(request,i):
#     if request.session['lin'] == "0":
#         return HttpResponse("<script>alert('your session has expired.please login again');window.location='/'</script>")
#     data = additionalinfo.objects.get(id=i)
#     return render(request,"STAFF/MOREDETAILSedit.html",{"data":data})

def editmoredetailsbutton(request,i):
    print("jjjjjjjjjjjjjjjjjjjjjjjjjjjjj")
    if request.session['lin'] == "0":
        return HttpResponse("<script>alert('your session has expired.please login again');window.location='/'</script>")
    btn  = request.POST['s']
    print(btn)
    if btn == 'Remove':
        additionalinfo.objects.get(id = i).delete()
        return HttpResponse("<script>alert('Deleted successfully');window.location='/inc#log'</script>")
    else:
        adno = request.POST['textfield']
        bg = request.POST['select3']
        hei = request.POST['textfield3']
        wei = request.POST['textfield4']
        rel = request.POST['select']
        cast = request.POST['select2']
        aain = request.POST['textfield8']
        ration = request.POST['select4']
        skill = request.POST['textarea']
        tenp = request.POST['textfield9']
        pltwop = request.POST['textfield10']
        lang = request.POST['textarea2']
        obj = additionalinfo.objects.get(id = i)
        obj.aadharno = adno
        obj.bloodg = bg
        obj.height = hei
        obj.weight = wei
        obj.religion = rel
        obj.caste = cast
        obj.annincome = aain
        obj.rationcard = ration
        obj.skills = skill
        obj.ten = tenp
        obj.plustwo = pltwop
        obj.languages = lang
        obj.save()
        return HttpResponse("<script>alert('Updated successfully');window.location='/inc#log'</script>")


def deletematerial(request,i):
    if request.session['lin'] == "0":
        return HttpResponse("<script>alert('your session has expired.please login again');window.location='/'</script>")
    material.objects.get(id=i).delete()
    return HttpResponse("<script>alert('Deleted successfully');window.location='/viewmaterial/"+str(request.session['aid'])+"'</script>")

def vieweventsst(request):
    if request.session['lin'] == "0":
        return HttpResponse("<script>alert('your session has expired.please login again');window.location='/'</script>")
    data = event.objects.all()
    return render(request,"STAFF/VIEW EVENT(S).html",{"data":data})

def viewnotistaff(request):
    if request.session['lin'] == "0":
        return HttpResponse("<script>alert('your session has expired.please login again');window.location='/'</script>")
    data = notification.objects.all()
    return render(request,"STAFF/VIEW NOTIFICATION(S).html",{"data":data})

def viewstudents(request):
    if request.session['lin'] == "0":
        return HttpResponse("<script>alert('your session has expired.please login again');window.location='/'</script>")
    data2 = sallocation.objects.filter(STAFF=request.session['sid'])
    return render(request,"STAFF/VIEW STUDENT.html",{"data2":data2})

def viewstudentsmark(request):
    if request.session['lin'] == "0":
        return HttpResponse("<script>alert('your session has expired.please login again');window.location='/'</script>")
    data2 = sallocation.objects.filter(STAFF=request.session['sid'])
    return render(request,"STAFF/STUDENT MARK.html",{"data2":data2})



def allocatedclasssub(request):
    if request.session['lin'] == "0":
        return HttpResponse("<script>alert('your session has expired.please login again');window.location='/'</script>")

    aid = request.POST['select1']
    h = request.POST['textfield2']
    btn = request.POST['e']
    if btn == 'Search':
        s = sallocation.objects.get(id = aid)
        data3 = student.objects.filter(semester=s.semester)
        data2 = sallocation.objects.filter(STAFF=request.session['sid'])
        return render(request,"STAFF/VIEW STUDENT.html",{"data":data3,"data2":data2})
    else:
        roll = request.POST.getlist('sid')
        atte = request.POST.getlist('c')
        for i in range(0,len(roll)):
            if roll[i] in atte:

                obj = attendance()
                obj.STUDENT_id = roll[i]
                obj.hour = h
                obj.SALLOCATION_id = aid
                obj.attend = 'Present'
                obj.date = datetime.datetime.now().date()
                obj.save()
            else:
                obj = attendance()
                obj.STUDENT_id = roll[i]
                obj.hour = h
                obj.SALLOCATION_id = aid
                obj.attend = 'absent'
                obj.date = datetime.datetime.now().date()
                obj.save()

        return HttpResponse("<script>alert('attendence added successfully');window.location='/sviewattendence'</script>")



def allocatedclassmark(request):
    if request.session['lin'] == "0":
        return HttpResponse("<script>alert('your session has expired.please login again');window.location='/'</script>")
    aid = request.POST['select1']
    b = request.POST['b']
    s = sallocation.objects.get(id=aid)

    if b == 'SEARCH':

        data3 = student.objects.filter(semester=s.semester)
        data2 = sallocation.objects.filter(STAFF=request.session['sid'])
        return render(request,"STAFF/STUDENT MARK.html",{"data":data3,"data2":data2})
    else:
        m = request.POST.getlist('e')
        sid = request.POST.getlist('sid')
        if len(mark.objects.filter(SALLOCATION_id = aid,semester=s.semester)) == 5:
            return HttpResponse("<script>alert('Already added');window.location='/viewstudentsmark'</script>")
        for i in range(0,len(m)):
            mobj = mark()
            mobj.STUDENT_id = sid[i]
            mobj.SALLOCATION_id = aid
            mobj.semester=s.semester
            mobj.type='Internal'
            mobj.mark=m[i]
            mobj.grade = request.POST['g']
            mobj.save()

        return HttpResponse("<script>alert('mark added successfully');window.location='/viewstudentsmark'</script>")
def sviewattendence(request):
    if request.session['lin'] == "0":
        return HttpResponse("<script>alert('your session has expired.please login again');window.location='/'</script>")
    data3 = sallocation.objects.filter(STAFF=request.session['sid'])
    return render(request, "STAFF/VIEW ATTENDENCE.html", {"data3":data3})

def sviewattendence_post(request):
    if request.session['lin'] == "0":
        return HttpResponse("<script>alert('your session has expired.please login again');window.location='/'</script>")
    data2 = attendance.objects.filter(SALLOCATION=request.POST['select1'],date=request.POST['d'])

    data3 = sallocation.objects.filter(STAFF=request.session['sid'])
    return render(request, "STAFF/VIEW ATTENDENCE.html", {"data2": data2,"data3":data3})


def editattendence(request,i):
    if request.session['lin'] == "0":
        return HttpResponse("<script>alert('your session has expired.please login again');window.location='/'</script>")
    data = attendance.objects.get(id=i)
    return render(request,"STAFF/ATTENDENCE MANAGEMENT EDIT.html",{"data":data})
def editattendencebutton(request,i):
    if request.session['lin'] == "0":
        return HttpResponse("<script>alert('your session has expired.please login again');window.location='/'</script>")
    att = request.POST['select1']
    obj = attendance.objects.get(id=i)
    obj.attend = att
    obj.save()
    return HttpResponse("<script>alert('Added successfully');window.location='/sviewattendence'</script>")
def attendencedelete(request,i):
    if request.session['lin'] == "0":
        return HttpResponse("<script>alert('your session has expired.please login again');window.location='/'</script>")
    attendance.objects.get(id=i).delete()
    return HttpResponse("<script>alert('Deleted successfully');window.location='/sviewattendence'</script>")

def viewmarks(request):
    if request.session['lin'] == "0":
        return HttpResponse("<script>alert('your session has expired.please login again');window.location='/'</script>")
    if request.method == 'POST':
        data = mark.objects.filter(STUDENT=request.POST['select2'])
        data3 = sallocation.objects.filter(STAFF=request.session['sid'])
        return render(request, "STAFF/VIEW MARK.html", {"data": data, "data3": data3})
    data3 = sallocation.objects.filter(STAFF=request.session['sid'])
    return render(request,"STAFF/VIEW MARK.html",{"data3":data3})

def regno1(request,i):
    if request.session['lin'] == "0":
        return HttpResponse("<script>alert('your session has expired.please login again');window.location='/'</script>")
    data3 = sallocation.objects.get(id = i)
    s = data3.semester
    c = student.objects.filter(semester=s)
    return render(request,"STAFF/reg.html",{"s":c})

def editmark(request,i):
    if request.session['lin'] == "0":
        return HttpResponse("<script>alert('your session has expired.please login again');window.location='/'</script>")
    data = mark.objects.get(id=i)
    return render(request, "STAFF/MARK MANAGEMENT.html", {"data": data})
def markeditbutton(request,i):
    if request.session['lin'] == "0":
        return HttpResponse("<script>alert('your session has expired.please login again');window.location='/'</script>")
    mar = request.POST['textfield4']
    gra = request.POST['textfield5']
    obj = mark.objects.get(id = i)
    obj.mark = mar
    obj.grade = gra
    obj.save()
    return HttpResponse("<script>alert('Edited successfully');window.location='/viewmarks'</script>")

def deletemark(request,i):
    if request.session['lin'] == "0":
        return HttpResponse("<script>alert('your session has expired.please login again');window.location='/'</script>")
    mark.objects.get(id=i).delete()
    return HttpResponse("<script>alert('Deleted successfully');window.location='/viewmarks'</script>")




def viewtimetables(request):
    if request.session['lin'] == "0":
        return HttpResponse("<script>alert('your session has expired.please login again');window.location='/'</script>")
    data = timetable.objects.filter(SALLOCATION__STAFF=request.session['sid'])
    # print(data,"hhhhhhhhhhhhhhhhhhhhhhhhhhhhh",request.session['sid'])
    mon =['nill','nill','nill','nill','nill']
    tue =['nill','nill','nill','nill','nill']
    wed =['nill','nill','nill','nill','nill']
    thu =['nill','nill','nill','nill','nill']
    fri =['nill','nill','nill','nill','nill']
    for i in data:
        print(i.day)
        if i.day == 'MONDAY':
            if i.hour == '1st Hour':
               mon[0]=i.SALLOCATION.SUBJECT.subjectname
            elif i.hour =='2nd Hour':
                mon[1] = i.SALLOCATION.SUBJECT.subjectname
            elif i.hour =='3rd Hour':
                mon[2] = i.SALLOCATION.SUBJECT.subjectname
            elif i.hour =='4th Hour':
                mon[3] = i.SALLOCATION.SUBJECT.subjectname
            else:
                mon[4] = i.SALLOCATION.SUBJECT.subjectname
        if i.day == 'TUESDAY':
            if i.hour == '1st Hour':
                tue[0] = i.SALLOCATION.SUBJECT.subjectname
            elif i.hour =='2nd Hour':
                tue[1] = i.SALLOCATION.SUBJECT.subjectname
            elif i.hour =='3rd Hour':
                tue[2] = i.SALLOCATION.SUBJECT.subjectname
            elif i.hour =='4th Hour':
                tue[3] = i.SALLOCATION.SUBJECT.subjectname
            else:
                tue[4] = i.SALLOCATION.SUBJECT.subjectname
        if i.day == 'WEDNESDAY':
            if i.hour == '1st Hour':
                wed[0] = i.SALLOCATION.SUBJECT.subjectname
            elif i.hour == '2nd Hour':
                wed[1] = i.SALLOCATION.SUBJECT.subjectname
            elif i.hour == '3rd Hour':
                wed[2] = i.SALLOCATION.SUBJECT.subjectname
            elif i.hour == '4th Hour':
                wed[3] = i.SALLOCATION.SUBJECT.subjectname
            else:
                wed[4] = i.SALLOCATION.SUBJECT.subjectname
        if i.day == 'THURSDAY':
            if i.hour == '1st Hour':
                thu[0] = i.SALLOCATION.SUBJECT.subjectname
            elif i.hour == '2nd Hour':
                thu[1] = i.SALLOCATION.SUBJECT.subjectname
            elif i.hour == '3rd Hour':
                thu[2] = i.SALLOCATION.SUBJECT.subjectname
            elif i.hour == '4th Hour':
                thu[3] = i.SALLOCATION.SUBJECT.subjectname
            else:
                thu[4] = i.SALLOCATION.SUBJECT.subjectname
        if i.day == 'FRIDAY':
            if i.hour == '1st Hour':
                fri[0] = i.SALLOCATION.SUBJECT.subjectname
            elif i.hour == '2nd Hour':
                fri[1] = i.SALLOCATION.SUBJECT.subjectname
            elif i.hour == '3rd Hour':
                fri[2] = i.SALLOCATION.SUBJECT.subjectname
            elif i.hour == '4th Hour':
                fri[3] = i.SALLOCATION.SUBJECT.subjectname
            else:
                fri[4] = i.SALLOCATION.SUBJECT.subjectname

    return render(request,"STAFF/VIEW TIME TABLE.html",{"m":mon,"t":tue,"w":wed,"th":thu,"f":fri})





################################ANDROID ##########################

def chaangepasswordst(request):
    if request.session['lin'] == "0":
        return HttpResponse("<script>alert('your session has expired.please login again');window.location='/'</script>")
    return render(request,"STAFF/CHANGE PASSWORD(S).html")
def chaangepasswordstbutton(request):
    if request.session['lin'] == "0":
        return HttpResponse("<script>alert('your session has expired.please login again');window.location='/'</script>")
    pw = request.POST['textfield']
    np = request.POST['textfield2']
    cp = request.POST['textfield3']
    if np == cp:
        data = login.objects.filter(password=pw,usertype='STAFF')
        if data.exists():
            data.update(password=np)
            return HttpResponse("<script>alert('password updated successfully');window.location='/'</script>")
        else:
            return HttpResponse("<script>alert('invalid details');window.location='/chaangepasswordst'</script>")
    else:
        return HttpResponse("<script>alert('password not valid');window.location='/chaangepasswordst'</script>")

def andchangepass(request):
    a = request.POST["a"]
    b = request.POST["b"]
    c = request.POST["c"]
    if b == c:
        data = login.objects.filter(password=a,id=request.POST['uid'])
        if data.exists():
            data.update(password=b)
            return JsonResponse({"status":"ok"})
        else:
            return JsonResponse({"status": "invalid details"})
    else:
        return JsonResponse({"status": "password not valid"})

def andlogin(request):
    u = request.POST["u"]
    p = request.POST["p"]
    q = login.objects.filter(username=u,password=p)
    print("",datetime.datetime.now().strftime('%A'))
    if q.exists():
        try:
            t = q[0].usertype
            # print(t,q[0].id)
            if t == 'student':
                sid = pallocation.objects.get(STUDENT__LOGIN=q[0].id)
                return JsonResponse({"status": "ok", "lid": sid.PARENT.id, "t": t,"uid":q[0].id, "d":datetime.datetime.now().strftime('%A').upper()})
            if t == 'parent':
                sid = parent.objects.get(LOGIN=q[0].id)
                return JsonResponse({"status": "ok", "lid": sid.id, "t": t,"uid":q[0].id, "d":datetime.datetime.now().strftime('%A').upper()})
        except :
            return JsonResponse({"status": "no"})

    else:
        return JsonResponse({"status":"no"})

def andsendcomp(request):
    a = request.POST['c']
    b = request.POST['d']
    id = request.POST['uid']
    obj = complaints()
    obj.cdescription = a
    obj.ctitle = b
    obj.parid = parent.objects.get(id=id)
    obj.stuid = student.objects.all()[0]
    obj.cdate = datetime.datetime.now().date()
    obj.creply='pending'
    obj.rdate='pending'
    obj.save()
    return JsonResponse({"status": "ok"})

def andviewreply(request):
    # print(request.POST['uid'])
    data = complaints.objects.filter(Q(parid=request.POST['lid']) | Q(stuid=request.POST['lid']))

    # Q(parid__LOGIN=request.POST['uid']) | Q(stuid__LOGIN=request.POST['uid'])
    users = []
    for i in data:

        users.append({
            'id': i.id,
            'ti': i.ctitle,
            'dis': i.cdescription,
            'date': i.cdate,
            'reply':i.creply,
            'replyd':i.rdate



        })
    return JsonResponse({"users": users, "status": "ok"})


def andviewattend(request):
    return JsonResponse()

def andviewevent(request):
    data = event.objects.all().order_by('-id')
    users = []
    for i in data:
        users.append({
            'id':i.id,
            'en':i.eventname,
            'ep':i.eventphoto,
            'ed':i.eventdate
        })
    return JsonResponse({"users":users,"status":"ok"})

def andviewmaark(request):
    s =  student.objects.get(id= request.POST['sid'])
    data2 = sallocation.objects.filter(semester=s.semester)
    users = []
    for i in data2:
        m1 = 0
        m = mark.objects.filter(SALLOCATION=i,STUDENT=s)
        for ij in m:
            m1 = m1+ij.mark
        a1 = 0
        a = attendance.objects.filter(SALLOCATION=i,STUDENT=s)
        for ij in a:
            if ij.attend == 'Present':
                a1 = a1+1

        users.append({
            'id':i.id,
            'sub': i.SUBJECT.subjectname,

            'mark': m1
        })



    return JsonResponse({"users":users,"status":"ok"})

def andviewmate(request):
    data = material.objects.filter(SALLOCATION=request.POST['mid'])
    users = []
    for i in data:
        users.append({
            'id': i.id,
            'ti': i.title,
            'mfi': i.mfile,
            

        })
    return JsonResponse({"users": users, "status": "ok"})


def andviewnoti(request):
    data = notification.objects.all().order_by('-id')
    users = []
    for i in data:
        users.append({
            'id': i.id,
            'ti': i.title,
            'di': i.discription,
            'da': i.date,
            'lin':i.link

        })
    return JsonResponse({"users": users, "status": "ok"})


def andviewprofile(request):
    data = student.objects.filter()
    users = []
    for i in data:
        p  = pallocation.objects.filter(PARENT=request.POST['uid'],STUDENT=i.id)
        if p.exists():
            users.append({
                'id': i.id,
                'na': i.studentname,
                'yr': i.year,
                'sem': i.semester,
                'dob': i.dateofbirth,
                'ad': i.admissionno,
                'reg': i.registerno,
                'ph':i.phonenumber,
                'sp':i.photo,
                'add':str(i.housename)+"\n"+str(i.place)+"\n"+str(i.postoffice)+"\n"+str(i.pincode),
                'em':i.emailid,
                'gd':str(i.guardianname)+"\n"+str(i.phonenumber)


            })
    return JsonResponse({"users": users, "status": "ok"})

def andviewsubandstaff(request):
    s =  student.objects.get(id= request.POST['uid'])
    data = sallocation.objects.filter(semester=s.semester)
    users = []
    for i in data:
        users.append({
            'id': i.id,
            'staffphoto': i.STAFF.photo,
            'sub': i.SUBJECT.subjectname,
            'staffname': i.STAFF.staffname,
            'number': i.STAFF.number,


            'syll': i.SUBJECT.subjectsyllubus,


        })
    return JsonResponse({"users": users, "status": "ok"})

def andtimetable(request):
    uid = request.POST['uid']
    d = request.POST['d']
    st = student.objects.get(LOGIN=uid)
    sem = st.semester
    t = timetable.objects.filter(SALLOCATION__semester=sem,day=d)

    d = ['nil','nil','nil','nil','nil']
    for i in t:
        if str(i.hour) == '1st Hour':
            d[0] =i.SALLOCATION.SUBJECT.subjectname
        if i.hour == '2nd Hour':
            d[1] = i.SALLOCATION.SUBJECT.subjectname
        if i.hour == '3rd Hour':
            d[2] = i.SALLOCATION.SUBJECT.subjectname
        if i.hour == '4th Hour':
            d[3] = i.SALLOCATION.SUBJECT.subjectname
        if i.hour == '5th Hour':
            d[4] = i.SALLOCATION.SUBJECT.subjectname


    return JsonResponse({"s1": d[0],"s2": d[1],"s3": d[2] ,"s4": d[3],"s5": d[4],"status":"ok"})



def andviewtutor(request):
    data = tutorallo.objects.all()
    users = []
    for i in data:
        users.append({
            'id': i.id,
            'name': i.STAFF.staffname,
            'tpic': i.STAFF.photo,
            'tphn': i.STAFF.number,
            'email': i.STAFF.email,
            'exp': i.STAFF.staffexperiance,
            'quali': i.STAFF.qualification
        })

        return JsonResponse({"users": users, "status": "ok"})

def andmark(request):
    s = student.objects.get(id=request.POST['sid'])
    data = mark.objects.filter(STUDENT_id=s).order_by('-id')
    users=[]
    for i in data:
        users.append({
            'id':i.id,
            'mark':i.mark,
            'grade':i.grade,
            'sub':i.SALLOCATION.SUBJECT.subjectname
        })
    
    return JsonResponse({"users": users,"status": "ok"})

def andattendence(request):
    s = student.objects.get(id=request.POST['sid'])
    print(s,"ssss")
    data = attendance.objects.filter(STUDENT_id=s).order_by('-id')
    users=[]
    d  = []
    for i in data:
        if i.date not in d:
            d.append(i.date)

    for i in d:
        c = attendance.objects.filter(STUDENT_id=s,date=i,attend='Present')
        if c.exists():
            if int(c.count()) <= 3 :
                users.append({
                    'id':c[0].id,
                    'attend': 'Half Day'+'('+str(c.count())+' '+'hours'+')',
                    'date':i
                })
            else:

                users.append({
                    'id': c[0].id,
                    'attend': 'Full Day'+'('+str(c.count())+' '+'hours'+')',
                    'date': i
                })
        else:
            users.append({
                'id': '0',
                'attend': 'Absent',
                'date': i
            })
    print("uuuu",users)
    return JsonResponse({ "status": "ok","users":users})

def andviewsemresults(request):

    s = student.objects.get(id=request.POST['sid'])
    data = externalmark.objects.filter(STUDENT=s)
    users = []
    for i in data:
        users.append({
            'id':i.id,
            'sem':i.semester,
            'typ':i.type,
            'file':i.file
        })
    return JsonResponse({"users":users, "status": "ok"})




    

