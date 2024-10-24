from django.shortcuts import render,redirect
from .models import *

# Create your views here.
def fun1(request):
    return render(request,"hi.html",{"name":"iza"})
def fun2(request):
    context = {
        'fruits' : ['apple','cherry','banana'],
    }
    return render(request,"fruit.html",context)
def fun3(request):
    item =[
        {'name':'apple','price':200,'quantity':10},
        {'name':'cherry','price':100,'quantity':10},
        {'name':'banana','price':200,'quantity':10},
    ]
    return render(request,"fruit3.html",{'items':item})
def fun4(request):
    item1=[
        {'name':'Laptop','price':999.99,'stock':'Instock'},
        {'name':'Smartphone','price':599.99,'stock':'Out ofstock'},
        {'name':'Tablet','price':299.99,'stock':'Instock'},
        {'name':'Headphone','price':149.99,'stock':'Instock'},
    ]
    return render(request,"products.html",{'item':item1})
def fun5(request):
    user=usermodel.objects.all()
    return render(request,"getall.html",{'user1':user})
def fun6(request):
    if request.method == 'POST':
        id=request.POST.get('id')
        name=request.POST.get('name')
        age=request.POST.get('age')
        user_obj=usermodel()
        user_obj.user_id=id
        user_obj.user_name=name
        user_obj.user_age=age
        user_obj.save()
        return redirect('my')
    return render(request,"add.html")
def fun7(request):
    prod=productmodel.objects.all()
    return render(request,"display.html",{'prod1':prod})
def fun8(request):
    if request.method == 'POST':
        name=request.POST.get('name')
        description=request.POST.get('des')
        price=request.POST.get('price')
        stock_quantity=request.POST.get('quantity')
        pro_object=productmodel()
        pro_object.product_name=name
        pro_object.product_description=description
        pro_object.product_price=price
        pro_object.stock_quantity=stock_quantity
        pro_object.save()

        return redirect('pic')
    return render(request,"add_product.html")
def fun9(request,id):
    prod=productmodel.objects.get(id=id)
    prod.delete()
    return redirect('pic')
def update(request,id):
    prod=productmodel.objects.get(id=id)
    if request.method == 'POST':
        name=request.POST.get('name')
        description=request.POST.get('des')
        price=request.POST.get('price')
        stock_quantity=request.POST.get('quantity')
        prod.product_name=name
        prod.product_description=description
        prod.product_price=price
        prod.stock_quantity=stock_quantity
        prod.save()
        return redirect('pic')
    return render(request,'update_prod.html',{'prod':prod})
def blog_model(request):
    blog=blogmodel.objects.all()
    return render(request,"display_blog.html",{'blog':blog})
def blogmodel1(request):
    if request.method =='POST':
        title=request.POST.get('title')
        content=request.POST.get('content')
        author=request.POST.get('author')
        blog_obj=blogmodel()
        blog_obj.title=title
        blog_obj.content=content
        blog_obj.author=author
        blog_obj.save()
        return redirect('post')
    return render("add_blog.html")
def updis(request):
    u=productusermodel.objects.all()
    return render(request,"display_userproduct.html",{'u1':u})
def updisadd(request):
   udata=usrproductmodel.objects.all()
   if request.method == 'POST':
       id=request.method.POST.get('id')
       pname=request.method.POST.get('pname')
       o=productusermodel()
       o.p_id=id
       o.p_name=pname
       o.usern=usermodel.objects.get(user_id=request.POST.get('user_id'))
       o.save()
       return redirect('agg')
   return render(request,"ADD PRODUCT.html",{'udata':udata})

    

    






def publish(request):
    publish=publishermodel.objects.all()
    return render(request,"displaypublisher.html",{'p1':publish})
def bookd(request):
    book=bookmodel.objects.all()
    return render(request,"display_bookdetails.html",{'b':book})

def delete(request,id):
    data=publishermodel.objects.get(id=id)
    data.delete()
    return redirect('bookd')
def update_publisher(request,id):
    data=publishermodel.objects.get(id=id)
    if request.method =='POST':
        name=request.POST.get('name')
        address=request.POST.get('address')
        email=request.POST.get('email')
        data.pu_name=name
        data.pu_address=address
        data.pu_email=email
        data.save()
        return redirect('bookd')
    return render(request,'update_publisherform.html',{'dataa':data}) 
def add_book(request):
    data=publishermodel.objects.all()
    if request.method =='POST':
        title=request.POST.get('title')
        date=request.POST.get('publication_date')
        isbn=request.POST.get('isbn')
        p=bookmodel()
        p.b_title=title
        p.publication_date=date
        p.isbn=isbn
        p.publisher=publishermodel.objects.get(id=request.POST.get('acc'))
        p.save()
        return redirect('bo')
    return render(request,'add_book.html',{'dataa':data})
def update_book_publisher(request,id):
    data=publishermodel.objects.all()
    data1=bookmodel.objects.get(id=id)
    if request.method == 'POST':
        title=request.POST.get('title')
        date=request.POST.get('date')
        isbn=request.POST.get('isbn')
        data1.b_title=title
        data1.publication_date=date
        data1.isbn=isbn
        data1.publisher=publishermodel.objects.get(id=request.POST.get('aaaa'))
        data1.save()
        return redirect('bo')
    return render(request,'book_publisher_update.html',{'data':data,'data1':data1})
def delete_book_publisher(request,id):
    obj=bookmodel.objects.get(id=id)
    obj.delete()
    return redirect('bo')
def  student1(request):
    student=studentmodel.objects.all()
    return render(request,"display_student.html",{'s':student})
def course1(request):
    course=Coursemodel.objects.all()
    return render(request,"display_course.html ",{'c':course})
def add_student(request):
    data=Coursemodel.objects.all()
    if request.method =='POST':
        first_name=request.POST.get('first_name')
        last_name=request.POST.get('last_name')
        Email=request.POST.get('Email')
        phone_number=request.POST.get('phone_number')
        
        s1=studentmodel()
        s1.first_name=first_name
        s1.last_name=last_name
        s1.Email=Email
        s1.phone_number=phone_number
        s1.course=Coursemodel.objects.get(id=request.POST.get('course'))
        
        s1.save()
        return redirect('zzz')
    return render(request,'add_new student.html',{"data1":data})
def updatestudent(request,id):
    data=studentmodel.objects.get(id=id)
    data1=Coursemodel.objects.all()
    if request.method =='POST':
        first_name=request.POST.get('first_name')
        last_name=request.POST.get('last_name')
        Email=request.POST.get('Email')
        phone_number=request.POST.get('phone_number')
        
        
        data.first_name=first_name
        data.last_name=last_name
        data.Email=Email
        data.phone_number=phone_number
        data.course=Coursemodel.objects.get(id=request.POST.get('course'))
        
        data.save()
        return redirect('vv')
    return render(request,'update student table.html',{'data':data,'data2':data1})
def deleteStudent(request,id):
    delete1=studentmodel.objects.get(id=id)
    delete1.delete()
    return redirect('vv')
def specific_student(request,id):
    data=studentmodel.objects.get(id=id)
    return render(request,'specific_student.html',{'specific':data}) 
def sepecific_course(request,id):
    c=Coursemodel.objects.get(id=id)
    data=studentmodel.objects.filter(course=c)
    return render(request,'dispaly_specific.html',{'dataa':data,'c1':c})



def organizer1(request):
    data=Organizermodel.objects.all()
    return render(request,'display_organizerR.html',{'o':data})
def Event1(request):
    ev=Eventmodel.objects.all()
    return render(request,'display_event.html ',{'e':ev})
def add_organizer(request):
    if request.method =='POST':
        name=request.POST.get('ID')
        email=request.POST.get('contact_email')
        number=request.POST.get('Phone_number')
        obj=Organizermodel()
        obj.Name=name
        obj.Contact_email=email
        obj.Phone_number=number
        obj.save()
        return redirect('YYY')
    return render(request,'add_organizer.html')
def add_event(request):
    org=Organizermodel.objects.all()
    if request.method == 'POST':
        title=request.POST.get('Title')
        date=request.POST.get('Date')
        location=request.POST.get('Location')
        obj=Eventmodel()
        obj.Title=title
        obj.Date=date
        obj.Location=location
        obj.organizer=Organizermodel.objects.get(id=request.POST.get('org'))
        obj.save()
        return redirect('displayevent')
    return render(request,'add_event.html',{'orgg':org})
def update_organizer(request,id):
    obj=Organizermodel.objects.get(id=id)
    if request.method == 'POST':
        name=request.POST.get('name')
        email=request.POST.get('email')
        number=request.POST.get('phone')
        obj.name=name
        obj.email=email
        obj.phone_number=number
        obj.save()
        return redirect('display_organizer')
    return render(request,'em_update_organizer.html',{'obj':obj})
def update_event(request,id):
    orgg=Organizermodel.objects.all()
    obj=Eventmodel.objects.get(id=id)
    if request.method == 'POST':
        title=request.POST.get('title')
        date=request.POST.get('date')
        location=request.POST.get('location')
        obj.Title=title
        obj.Date=date
        obj.Location=location
        obj.organizer=Organizermodel.objects.get(id=request.POST.get('org'))
        obj.save()
        return redirect('display_event')
    return render(request,'em_update_event.html',{'obj':obj,'organize':orgg})
def delete_organizer(request,id):
    dlt=Organizermodel.objects.get(id=id)
    dlt.delete()
    return redirect('display_organizer')
def delete_event(request,id):
    dlt=Eventmodel.objects.get(id=id)
    dlt.delete()
    return redirect('display_event')

        


   













        










        







    












