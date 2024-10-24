"""
URL configuration for django1 project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from app import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('b',views.fun1),
    path('c',views.fun2),
    path('d',views.fun3),
    path('e',views.fun4),
    path('f',views.fun5,name='my'),
    path('g',views.fun6),
    path('i',views.fun8),
    path('h',views.fun7,name='pic'),
    path('j\<int:id>',views.fun9,name='delete_product'),
    path('update\<int:id>',views.update,name='update_prod'),
    path('bl',views.blog_model),
    path('b1',views.blogmodel1,name='post'),
    path('up',views.updis),
    path('pu',views.publish,name='bookd'),
    path('bd',views.bookd,name='bo'),
    path('ii',views.add_book),
    path('delete_publisher/<int:id>',views.delete,name='delete_publisherr'),
    path('update_publisherr/<int:id>',views.update_publisher ,name='update_publisherr'),
    path('update_book_publisher/<int:id>',views.update_book_publisher,name='update_book'),
    path('delete_book_publisher/<int:id>',views.delete_book_publisher,name="delete_book"),
    path('student',views.student1,name='vv'),
    path('course',views.course1),
    path('jj',views.add_student,name='zzz'),
    path('updateStudent/<int:id>',views.updatestudent,name='updateStudent'),
    path('deleteStudent/<int:id>',views.deleteStudent,name='deleteStudent'),
    path('specific/<int:id>',views.specific_student,name='zss'),
    path('display/<int:id>',views.sepecific_course),
    path('oraganizer',views.organizer1),
    path('event',views.Event1),
    path('addorg',views.add_organizer),
    path('addevent',views.add_event),
    path('update_organizer/<int:id>',views.update_organizer,name='update_organizer'),
    path('update_event/<int:id>',views.update_event,name='update_event'),
    path('delete_organizer/<int:id>',views.delete_organizer,name='delete_organizer'),
    path('delete_event/<int:id>',views.delete_event,name='delete_event'),

]