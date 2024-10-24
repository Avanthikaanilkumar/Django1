from django.contrib import admin
from .models import *
# Register your models here.
admin.site.register(usermodel)
class prodadmin(admin.ModelAdmin):
    list_display=('product_name','product_description','product_price')
    search_fields=('product_name',)
    list_filter=('product_name',)
admin.site.register(productmodel,prodadmin)
admin.site.site_header='MY_SITE'
admin.site.site_title='Django_site'

admin.site.register(usrproductmodel)
admin.site.register(productusermodel)
admin.site.register(publishermodel)
class bookadmin(admin.ModelAdmin):
    list_display=('b_title','isbn','publisher')
    search_fields=('b_title','isbn',)
    list_filter=('publication_date',)

admin.site.register(bookmodel,bookadmin)
class studentadmin(admin.ModelAdmin):
    list_display=('first_name','last_name','Email','phone_number')
admin.site.register(studentmodel)
admin.site.register(Coursemodel)
admin.site.register(Organizermodel)
admin.site.register(Eventmodel)
