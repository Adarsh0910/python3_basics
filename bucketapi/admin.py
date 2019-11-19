from django.contrib import admin
from . import models

# Register your models here.

class BucketapiAdmin(admin.ModelAdmin):
    list_display = ("name",  "date_created", "date_modified")

admin.site.register(models.Bucketlist, BucketapiAdmin)
#admin.site.register(models.Category, CategoryAdmin)

