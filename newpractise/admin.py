from django.contrib import admin

# Register your models here.
from .models import NewProject

admin.site.register(NewProject)
#MTV(model, tehmplate, view)패턴