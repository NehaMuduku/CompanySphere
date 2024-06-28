from django.contrib import admin

# Register your models here.
#from .models import HiringData
#admin.site.register(HiringData)
from django.contrib import admin
from .models import FreshersData

admin.site.register(FreshersData)

