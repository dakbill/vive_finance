from django.contrib import admin
from susu.models import Member, Account, Voucher


class VoucherAdmin(admin.ModelAdmin):
    list_filter = ['used']


admin.site.register(Member)
admin.site.register(Account)
admin.site.register(Voucher, VoucherAdmin)
