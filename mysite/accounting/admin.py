from django.contrib import admin

from .models import *

# Register your models here.

admin.site.register(MyUser)
admin.site.register(Member)
admin.site.register(TransactionType)
admin.site.register(Issue)
admin.site.register(Transaction)