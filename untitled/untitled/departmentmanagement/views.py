import datetime
from django.core.files.storage import FileSystemStorage
from django.http import HttpResponse
from django.shortcuts import render
from departmentmanagement.models import *
# Create your views here.

def logins(request):
    return render(request,"login.html")
def loginsbutton(request):
    un = request.POST['textfield']
    pw = request.POST['textfield2']
    ut = request.POST['textfield3']
    lobj = login()
    lobj.username = un
    lobj.password = pw
    lobj.usertype = ut
    lobj.save()
    print(un,pw)
    return HttpResponse("<script>alert('Added successfully');window.location='/logins'</script>")




def chaangepassword(request):
    return render(request,"admin/CHANGE PASSWORD.html")
def chaangepasswordbutton(request):
    pw = request.POST['textfield']
    np = request.POST['textfield2']
    cp = request.POST['textfield3']
    print(pw,np,cp)
    return "submit"

#
# def complaintmanagement(request):
#     return render(request,"admin/COMPLAINT MANAGEMENT.html")
# def complaintmanagementbutton(request):
#     title = request.POST['textfield']
#     dis = request.POST['textarea']
#     date = request.POST['textfield2']
#     rp = request.POST['textarea2']
#     rd = request.POST['textfield3']
#     cobj =complaints()
#     cobj.ctitle = title
#     cobj.cdescription = dis
#     cobj.cdate = date
#     cobj.creply = rp
#     cobj.rdate = rd
#     cobj.save()
#     print(title,dis,date,rp,rd)
#     return HttpResponse("<script>alert('Added successfully');window.location='/complaintmanagement'</script>")
#
def replymanagement(request):
    return render(request,"admin/REPLY MANAGEMENT.html")
def replymanagementbutton(request):
    repl = request.POST['textarea']
    replyd = request.POST['textfield']
    robj = complaints()
    robj.creply = repl
    robj.rdate = replyd
    robj.save()

    return HttpResponse("<script>alert('Added successfully');window.location='/replymanagement'</script>")


def eventmanagement(request):
    return render(request,"admin/EVENT MANAGEMENT.html")
def eventmanagementbutton(request):
    en = request.POST['textfield']
    ep = request.FILES['fileField']
    ed = request.POST['textfield2']
    fs = FileSystemStorage()
    d = datetime.datetime.now().strftime("%Y%m%d%H%M%S")
    fs.save(r"C:\Users\id\PycharmProjects\untitled\departmentmanagement\static\file\\"+d+'.jpg',ep)
    eobj = event()
    eobj.eventname = en
    eobj.eventdate = ed
    eobj.eventphoto = '/static/file/'+d+'.jpg'
    eobj.save()
    print(en, ep, ed)
    return HttpResponse("<script>alert('Added successfully');window.location='/eventmanagement'</script>")

def notificationmanagement(request):
    return render(request,"admin/NOTIFICATION MANAGEMENT.html")
def notificationmanagementbutton(request):
    tit = request.POST['textfield']
    dis = request.POST['textarea']
    dat = request.POST['textfield2']
    nobj = notification()
    nobj.title = tit
    nobj.discription = dis
    nobj.date = dat
    nobj.save()
    return HttpResponse("<script>alert('Added successfully');window.location='/notificationmanagement'</script>")


def parentallocation(request):
    return render(request,"admin/PARENT ALLOCATION.html")
def parentallocationbutton(request):
    par = request.POST['select']
    stu = request.POST['select2']
    pob1 = pallocation()
    pob1.PARENT = par
    pob1.STUDENT = stu
    pob1.save()
    return HttpResponse("<script>alert('Added successfully');window.location='/parentallocation'</script>")

def parentmanagement(request):
    return render(request,"admin/PARENT MANAGEMENT.html")
def parentmanagementbutton(request):
    pn = request.POST['textfield']
    pp = request.POST['textfield2']
    pe = request.POST['textfield3']
    paobj = parent()
    paobj.parentname = pn
    paobj.phoneno = pp
    paobj.emailid = pe
    paobj.save()
    return HttpResponse("<script>alert('Added successfully');window.location='/parentmanagement'</script>")


def staffmanagement(request):
    return render(request,"admin/STAFF MANAGEMENT.html")
def staffmanagementbutton(request):
    sn = request.POST['textfield']
    sp = request.FILES['file']
    sq = request.POST['textarea']
    sno = request.POST['textfield2']
    sem = request.POST['textfield3']
    sex = request.POST['textarea2']
    spst = request.POST['textfield4']
    fs = FileSystemStorage()
    d = datetime.datetime.now().strftime("%y%m%d%H%M%S")
    fs.save(r"C:\Users\id\PycharmProjects\untitled\departmentmanagement\static\file\\"+d+'.jpg',sp)
    sobj = staff()
    sobj.staffname = sn
    sobj.photo = '/static/file/'+d+'.jpg'
    sobj.qualification = sq
    sobj.number = sno
    sobj.email = sem
    sobj.staffexperiance = sex
    sobj.post = spst
    sobj.save()
    return HttpResponse("<script>alert('Added successfully');window.location='/staffmanagement'</script>")

def studentmanagement(request):
    return render(request,"admin/STUDENT MANAGEMENT.html")
def studentmanagementbutton(request):
    sn = request.POST['textfield']
    sy = request.POST['textfield2']
    ssem = request.POST['textfield14']
    sdob = request.POST['textfield6']
    adn = request.POST['textfield3']
    regn = request.POST['textfield4']
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
    fs.save(r"C:\Users\id\PycharmProjects\untitled\departmentmanagement\static\file\\" + d + '.jpg', sp)
    sob1 = student()
    sob1.studentname = sn
    sob1.year = sy
    sob1.semester = ssem
    sob1.dateofbirth = sdob
    sob1.admissionno = adn
    sob1.registerno = regn
    sob1.phoneno = phn
    sob1.photo = '/static/file/'+d+'.jpg'
    sob1.emailid = se
    sob1.housename = sh
    sob1.place = spl
    sob1.postoffice = spost
    sob1.pincode = spin
    sob1.guardianname = sgn
    sob1.phonenumber = sgph
    sob1.save()
    return HttpResponse("<script>alert('Added successfully');window.location='/studentmanagement'</script>")

def viewattendence(request):
    data = attendance.objects.all()
    return render(request,"admin/VIEW ATTENDENCE.html",{"data":data})



def subjectallocation(request):
    return render(request,"admin/SUBJECT ALLOCATION.html")
def subjectallocationbutton(request):
    ss = request.POST['select']
    ssem = request.POST['textfield']
    ssub = request.POST['select2']
    sob2 = sallocation()
    sob2.STAFF = ss
    sob2.semester = ssem
    sob2.SUBJECT = ssub
    sob2.save()
    return HttpResponse("<script>alert('Added successfully');window.location='/subjectallocation'</script>")

def subjectmanagement(request):
    return render(request,"admin/SUBJECT MANAGEMENT.html")
def subjectmanagementbutton(request):
    sn = request.POST['textfield']
    sc = request.POST['textfield2']
    ss = request.FILES['fileField']
    sem = request.POST['textfield3']
    fs = FileSystemStorage()
    d = datetime.datetime.now().strftime("%y%m%d%H%M%S")
    fs.save(r"C:\Users\id\PycharmProjects\untitled\departmentmanagement\static\file\\" + d + '.pdf', ss)
    smobj = subject()
    smobj.subjectname = sn
    smobj.subjectcode = sc
    smobj.subjectsyllubus = '/static/file/'+d+'.pdf'
    smobj.semester = sem
    smobj.save()
    return HttpResponse("<script>alert('Added successfully');window.location='/subjectmanagement'</script>")


def timetablemanagement(request):
    return render(request,"admin/TIME TABLE MANAGEMENT.html")
def timetablemanagementbutton(request):
    day = request.POST['select']
    hr = request.POST['textfield2']
    sub = request.POST['select2']
    tobj = timetable()
    tobj.day = day
    tobj.hour = hr
    tobj.subject = sub
    tobj.save()
    return HttpResponse("<script>alert('Added successfully');window.location='/timetablemanagement'</script>")

def viewcomplaints(request):
    data = complaints.objects.all()
    return render(request,"admin/VIEW COMPLAINTS.html",{"data":data})

def viewevents(request):
    data = event.objects.all()
    return render(request,"admin/VIEW EVENT.html",{"data":data})

def viewmark(request):
    data = mark.objects.all()
    return render(request,"admin/VIEW MARK.html",{"data":data})

def viewnotification(request):
    data = notification.objects.all()
    return render(request,"admin/VIEW NOTIFICATION.html",{"data":data})

def viewpallocation(request):
    data = pallocation.objects.all()
    return render(request,"admin/VIEW PARENT ALLOCATION.html",{"data":data})

def viewparent(request):
    data = parent.objects.all()
    return render(request,"admin/VIEW PARENT.html",{"data":data})

def viewstaff(request):
    data = staff.objects.all()
    return render(request,"admin/VIEW STAFF.html",{"data":data})

def viewstudent(request):
    data = student.objects.all()
    return render(request,"admin/VIEW STUDENT.html",{"data":data})

def viewsubject(request):
    data = subject.objects.all()
    return render(request,"admin/VIEW SUBJECT.html",{"data":data})

def viewtimetable(request):
    data = timetable.objects.all()
    return render(request,"admin/VIEW TIME TABLE.html",{"data":data})


def adminhomepage(request):
    return render(request,"admin/HOME.html")

def viewsubjectallocation(request):
    data = sallocation.objects.all()
    return render(request,"admin/VIEW SUBJECT ALLOCATION.html",{"data":data})

#def deletecomplaints(request):
 #   complaints.objects.get(id=id).delete()
  #  return HttpResponse("<script>alert('Deleted successfully');window.location='/viewcomplaints'</script>")
def deleteevent(request,id):
    event.objects.get(id=id).delete()
    return HttpResponse("<script>alert('Deleted successfully');window.location='/viewevents'</script>")
def deletenotifi(request,id):
    notification.objects.get(id=id).delete()
    return HttpResponse("<script>alert('Deleted successfully');window.location='/viewnotification'</script>")
def deletepallo(request,id):
    pallocation.objects.get(id=id).delete()
    return HttpResponse("<script>alert('Deleted successfully');window.location='/viewpallocation'</script>")
def deleteparent(request,id):
    parent.objects.get(id=id).delete()
    return HttpResponse("<script>alert('Deleted successfully');window.location='/viewparent'</script>")
def deletestaff(request,id):
    staff.objects.get(id = id).delete()
    return HttpResponse("<script>alert('Deleted successfully');window.location='/viewstaff'</script>")
def deletestudent(request,id):
    student.objects.get(id=id).delete()
    return HttpResponse("<script>alert('Deleted successfully');window.location='/viewstudent'</script>")
def deletesub(request,id):
    subject.objects.get(id=id).delete()
    return HttpResponse("<script>alert('Deleted successfully');window.location='/viewsubject'</script>")
def deletesuballo(request,id):
    sallocation.objects.get(id=id).delete()
    return HttpResponse("<script>alert('Deleted successfully');window.location='/viewsubjectallocation'</script>")
def deletetimetable(request,id):
    timetable.objects.get(id=id).delete()
    return HttpResponse("<script>alert('Deleted successfully');window.location='/viewtimetable'</script>")



def editevent(request,id):
    data = event.objects.get(id=id)
    return render(request,"admin/EVENT EDIT.html",{"data":data})
def eventeditbutton(request,id):
    en = request.POST['textfield']
    ep = request.FILES['fileField']
    ed = request.POST['textfield2']
    fs = FileSystemStorage()
    d = datetime.datetime.now().strftime("%Y%m%d%H%M%S")
    fs.save(r"C:\Users\id\PycharmProjects\untitled\departmentmanagement\static\file\\"+d+'.jpg',ep)
    eobj = event.objects.get(id=id)
    eobj.eventname = en
    eobj.eventdate = ed
    eobj.eventphoto = '/static/file/'+d+'.jpg'
    eobj.save()
    print(en, ep, ed)
    return HttpResponse("<script>alert('Added successfully');window.location='/viewevents'</script>")

def editnoti(request, id):
    data = notification.objects.get(id=id)
    return render(request, "admin/NOTIFICATION EDIT.html",{"data":data})
def editpalloc(request,id):
    data = pallocation.objects.get(id=id)
    return render(request,"admin/PARENT ALLOCAEDIT.html",{"data":data})
def editparent(request,id):
    data = parent.objects.get(id=id)
    return render(request,"admin/PARENT MANAGEMENTEDIT.html",{"data":data})
def editstaff(request,id):
    data = staff.objects.get(id=id)
    return render(request,"admin/STAFF MANAGEMENTEDIT.html",{"data":data})
def editstud(request,id):
    data = student.objects.get(id=id)
    return render(request,"admin/STUDENT MANAGEMENTEDIT.html",{"data":data})
def editsuballo(request,id):
    data = sallocation.objects.get(id=id)
    return render(request,"admin/SUBJECT ALLOCATIONEDIT.html",{"data":data})
def editsub(request,id):
    data = subject.objects.get(id=id)
    return render(request,"admin/SUBJECT MANAGEMENTEDIT.html",{"data":data})
def edittt(request,id):
    data = timetable.objects.get(id=id)
    return render(request,"admin/TIME TABLE MANAGEMENTEDIT.html",{"data":data})