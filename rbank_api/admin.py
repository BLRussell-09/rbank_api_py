from django.contrib import admin
from .models import Account, Member, Share, Transaction
# Register your models here.

admin.site.register(Account)
admin.site.register(Member)
admin.site.register(Share)
admin.site.register(Transaction)