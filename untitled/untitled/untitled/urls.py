"""untitled URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from departmentmanagement import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('logins',views.logins),
    path('loginsbutton',views.loginsbutton),
    path('chaangepassword',views.chaangepassword),
    path('chaangepasswordbutton',views.chaangepasswordbutton),
   # path('complaintmanagement',views.complaintmanagement),
   # path('complaintmanagementbutton',views.complaintmanagementbutton),
    path('eventmanagement',views.eventmanagement),
    path('eventmanagementbutton',views.eventmanagementbutton),
    path('notificationmanagement',views.notificationmanagement),
    path('notificationmanagementbutton',views.notificationmanagementbutton),
    path('parentallocation',views.parentallocation),
    path('parentallocationbutton',views.parentallocationbutton),
    path('parentmanagement',views.parentmanagement),
    path('parentmanagementbutton',views.parentmanagementbutton),
    path('staffmanagement',views.staffmanagement),
    path('staffmanagementbutton',views.staffmanagementbutton),
    path('studentmanagement',views.studentmanagement),
    path('studentmanagementbutton',views.studentmanagementbutton),
    path('subjectallocation', views.subjectallocation),
    path('subjectallocationbutton', views.subjectallocationbutton),
    path('subjectmanagement', views.subjectmanagement),
    path('subjectmanagementbutton', views.subjectmanagementbutton),
    path('timetablemanagement', views.timetablemanagement),
    path('timetablemanagementbutton', views.timetablemanagementbutton),
    path('viewattendence',views.viewattendence),
    path('viewcomplaints', views.viewcomplaints),
    path('viewevents', views.viewevents),
    path('viewmark', views.viewmark),
    path('viewnotification', views.viewnotification),
    path('viewpallocation', views.viewpallocation),
    path('viewparent', views.viewparent),
    path('viewstaff', views.viewstaff),
    path('viewstudent', views.viewstudent),
    path('viewsubject', views.viewsubject),
    path('viewtimetable', views.viewtimetable),
    path('adminhomepage', views.adminhomepage),
    path('viewsubjectallocation',views.viewsubjectallocation),
    path('replymanagement',views.replymanagement),
    path('replymanagementbutton',views.replymanagementbutton),

    path('deleteevent/<id>',views.deleteevent),
    path('deletenotifi/<id>',views.deletenotifi),
    path('deletepallo/<id>',views.deletepallo),
    path('deleteparent/<id>',views.deleteparent),
    path('deletestaff/<id>',views.deletestaff),
    path('deletestudent/<id>',views.deletestudent),
    path('deletesub/<id>',views.deletesub),
    path('deletesuballo/<id>',views.deletesuballo),
    path('deletetimetable/<id>',views.deletetimetable),


    path('editevent/<id>',views.editevent),
    path('editnoti/<id>',views.editnoti),
    path('editpalloc/<id>',views.editpalloc),
    path('editparent/<id>',views.editparent),
    path('editstaff/<id>',views.editstaff),
    path('editstud/<id>',views.editstud),
    path('editsuballo/<id>',views.editsuballo),
    path('editsub/<id>',views.editsub),
    path('edittt/<id>',views.edittt),


    path('eventeditbutton/<id>',views.eventeditbutton),







]
