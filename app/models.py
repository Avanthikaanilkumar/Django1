from django.db import models

# Create your models here.
class usermodel(models.Model):
    user_id=models.IntegerField(primary_key=True)
    user_name=models.CharField(max_length=100)
    user_age=models.IntegerField() 
class productmodel(models.Model):
    product_name=models.CharField(max_length=100)
    product_description=models.TextField()
    product_price=models.DecimalField(max_digits=10,decimal_places=2)
    stock_quantity=models.IntegerField()
    created_at=models.DateTimeField(auto_now=True)
class blogmodel(models.Model):
    title=models.CharField(max_length=100)
    content=models.CharField(max_length=100)
    author=models.CharField(max_length=100)
    created_at=models.DateTimeField(auto_now=True)
    updated_at=models.DateTimeField(auto_now=True)
class usrproductmodel(models.Model):
    user_id=models.IntegerField(primary_key=True)
    user_name=models.CharField(max_length=100)
    user_age=models.IntegerField()
    def __str__(self):
        return self.user_name
class productusermodel(models.Model):
    p_id=models.IntegerField(primary_key=True)
    p_name=models.CharField(max_length=100)
    up_name=models.ForeignKey(usrproductmodel,on_delete=models.CASCADE)
class publishermodel(models.Model):
    
    pu_name=models.CharField(max_length=100)
    pu_address=models.CharField(max_length=100)
    pu_email=models.EmailField()
    def __str__(self):
        return self.pu_name
class bookmodel(models.Model):
    b_title=models.CharField(max_length=100)
    publication_date=models.DateField()
    isbn=models.CharField(max_length=100,unique=True)
    publisher=models.ForeignKey(publishermodel,on_delete=models.CASCADE)

class Coursemodel(models.Model):
    course_name=models.CharField(max_length=100)
    course_code=models.IntegerField(unique=True)
    Date=models.DateField()
    def __str__(self):
        return self.course_name

class studentmodel(models.Model):
    first_name=models.CharField(max_length=100)
    last_name=models.CharField(max_length=100)
    Email=models.EmailField(unique=True)
    phone_number=models.CharField(max_length=100)
    course=models.ForeignKey(Coursemodel,on_delete=models.CASCADE)
    def __str__(self):
        return self.first_name
class Organizermodel(models.Model):
    ID=models.AutoField(primary_key=True)
    Name=models.CharField(max_length=100)
    Contact_email=models.EmailField(unique=True)
    Phone_number=models.CharField(max_length=15)
    def __str__(self):
        return self.Name
class Eventmodel(models.Model):
    Event_id=models.AutoField(primary_key=True)
    Title=models.CharField(max_length=200)
    Date=models.DateTimeField()
    Location=models.CharField(max_length=255)
    organizer=models.ForeignKey(Organizermodel,on_delete=models.CASCADE)
    def __str__(self):
        return self.Event_id

    


