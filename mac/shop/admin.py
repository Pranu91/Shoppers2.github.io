from django.contrib import admin

# Register your models here.

from.models import product,contact,Orders,OrderUpdate

admin.site.register(product)
admin.site.register(contact)
admin.site.register(Orders)
admin.site.register(OrderUpdate)