from django.contrib import admin
from .models import Products, OSAGO, KASKO, NS, Klezh, IFL, Mortgage, OrderStatus


# Register your models here.
admin.site.register(Products)
admin.site.register(OSAGO)
admin.site.register(KASKO)
admin.site.register(NS)
admin.site.register(Klezh)
admin.site.register(IFL)
admin.site.register(Mortgage)
admin.site.register(OrderStatus)
