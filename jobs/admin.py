from django.contrib import admin
from .models import Jobs, Skills, Currency,Budget
# Register your models here.


admin.site.register(Jobs)
admin.site.register(Skills)
admin.site.register(Currency)
admin.site.register(Budget)