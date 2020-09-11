from django.contrib import admin
from .models import Test,Value,Record,Application,Device,Profile,new
# Register your models here.
admin.site.register(Test)
admin.site.register(Value)
admin.site.register(Application)
admin.site.register(Record)
admin.site.register(Device)
admin.site.register(Profile)