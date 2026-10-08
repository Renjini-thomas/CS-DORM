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
    path('',views.logins),
    path('searchsem',views.searchsem),
    path('loginsbutton',views.loginsbutton),
    path('chaangepassword',views.chaangepassword),
    path('chaangepasswordbutton',views.chaangepasswordbutton),
   # path('complaintmanagement',views.complaintmanagement),
   # path('complaintmanagementbutton',views.complaintmanagementbutton),
    path('eventmanagement',views.eventmanagement),
    path('eventmanagementbutton',views.eventmanagementbutton),
    path('notificationmanagement',views.notificationmanagement),
    path('notificationmanagementbutton',views.notificationmanagementbutton),
    path('parentallocation/<i>',views.parentallocation),
    path('parentallocationbutton/<i>/<p>',views.parentallocationbutton),
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
    path('searchmark', views.searchmark),
    path('viewnotification', views.viewnotification),
    path('viewpallocation/<i>', views.viewpallocation),
    path('viewparent', views.viewparent),
    path('viewstaff', views.viewstaff),
    path('viewstudent', views.viewstudent),
    path('viewsubject', views.viewsubject),
    path('viewtimetable', views.viewtimetable),
    path('adminhomepage', views.adminhomepage),
    path('viewsubjectallocation',views.viewsubjectallocation),
    path('replymanagement/<id>',views.replymanagement),
    path('replymanagementbutton/<id>',views.replymanagementbutton),

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
    path('notificationeditbutton/<id>',views.notificationeditbutton),
    path('parentallocationeditbutton/<id>',views.parentallocationeditbutton),
    path('parentmanagementeditbutton/<id>',views.parentmanagementeditbutton),
    path('staffmanagementeditbutton/<id>',views.staffmanagementeditbutton),
    path('studentmanagementeditbutton/<id>',views.studentmanagementeditbutton),
    path('subjectallocationeditbutton/<id>',views.subjectallocationeditbutton),
    path('subjectmanagementeditbutton/<id>',views.subjectmanagementeditbutton),
    path('timetablemanagementeditbutton/<id>',views.timetablemanagementeditbutton),




    path('allocacatedsubjects',views.allocacatedsubjects),
    path('STAFFhomepage',views.STAFFhomepage),
    path('materialmanagement/<i>',views.materialmanagement),
    path('materialmanagementbutton/<i>',views.materialmanagementbutton),
    path('viewmaterial/<i>',views.viewmaterial),
    path('materialmanagementeditbutton/<i>',views.materialmanagementeditbutton),
    path('editmaterial/<i>',views.editmaterial),
    path('deletematerial/<i>',views.deletematerial),
    path('vieweventsst',views.vieweventsst),
    path('viewnotistaff',views.viewnotistaff),
    path('viewstudents',views.viewstudents),
    path('viewtimetables',views.viewtimetables),
    path('chaangepasswordstbutton',views.chaangepasswordstbutton),
    path('chaangepasswordst',views.chaangepasswordst),
    path('allocatedclasssub',views.allocatedclasssub),
    path('viewstudentsmark',views.viewstudentsmark),
    path('allocatedclassmark',views.allocatedclassmark),
    path('viewmarks',views.viewmarks),
    path('editmark/<i>',views.editmark),
    path('markeditbutton/<i>',views.markeditbutton),
    path('deletemark/<i>',views.deletemark),
    path('sviewattendence',views.sviewattendence),
    path('searchattend',views.searchattend),
    path('editattendence/<i>',views.editattendence),
    path('editattendencebutton/<i>',views.editattendencebutton),
    path('attendencedelete/<i>',views.attendencedelete),
    path('logout',views.logout),
    path('sviewattendence_post',views.sviewattendence_post),
    path('regno/<i>',views.regno1),

    path('andchangepass',views.andchangepass),
    path('andlogin',views.andlogin),
    path('andsendcomp',views.andsendcomp),
    path('andviewreply',views.andviewreply),
    path('andviewattend',views.andviewattend),
    path('andviewevent',views.andviewevent),
    path('andviewmaark',views.andviewmaark),
    path('andviewmate',views.andviewmate),
    path('andviewnoti',views.andviewnoti),
    path('andviewprofile',views.andviewprofile),
    path('andviewsubandstaff',views.andviewsubandstaff),
    path('andtimetable',views.andtimetable),
    path('tutorallobutton',views.tutorallobutton),
    path('tutorallocation',views.tutorallocation),
    path('viewtutorallo',views.viewtutorallo),
    path('externalmarkbutton/<s>',views.externalmarkbutton),
    path('externalmarkuniv/<id>',views.externalmarkuniv),
    path('viewexternal/<i>',views.viewexternal),
    path('inc',views.inc),
    path('incsearch',views.incsearch),
    path('deleteexternalmark/<i>',views.deleteexternalmark),
    path('deletetutoralloc/<i>',views.deletetutoralloc),
    path('moredetailsbutton/<s>',views.moredetailsbutton),
    path('moredetails/<i>',views.moredetails),
    path('viewmoredetails/<i>',views.viewmoredetails),
    path('editmoredetailsbutton/<i>',views.editmoredetailsbutton),
    # path('editmoredetails/<i>',views.editmoredetails),
    path('deletemoredetails/<i>',views.deletemoredetails),
    path('andviewsemresults',views.andviewsemresults),
    path('andviewtutor',views.andviewtutor),
    path('andmark',views.andmark),
    path('andattendence',views.andattendence),

    path('viewstudent_post',views.viewstudent_post),
    path('searchrecord',views.searchrecord),
    path('searchpost',views.searchpost),
    path('searchmore/<id>',views.searchmore),
    path('searchpostallo',views.searchpostallo),
    path('andviewsemresults',views.andviewsemresults),







]
