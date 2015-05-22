from django.contrib import admin
from models import Dataset, Attribute, Label

# Register your models here.
admin.site.register(Dataset)
admin.site.register(Attribute)
admin.site.register(Label)
