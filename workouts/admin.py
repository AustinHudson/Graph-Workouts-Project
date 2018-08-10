from django.contrib import admin
from .models import Exercises, People, Routines, ExerciseInRoutine
# Register your models here.

admin.site.register(Exercises)

admin.site.register(Routines)

admin.site.register(People)

admin.site.register(ExerciseInRoutine)