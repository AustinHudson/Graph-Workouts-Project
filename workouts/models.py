from django.db import models



# Create your models here.

class Routines(models.Model):
    routine_name = models.CharField(max_length=100)
    routine_description = models.TextField(max_length=200)

class Exercises(models.Model):
    exercise_name = models.CharField(max_length=100)
    description = models.TextField(max_length=200)

#
# Change this to many to many field in other classes
#
# class Routine_Exercises(models.Model):
#
#     default_sets = models.IntegerField
#     default_reps = models.IntegerField
#
#
#
