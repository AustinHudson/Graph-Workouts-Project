from django.db import models
from django.contrib.auth.models import User





class Exercises(models.Model):
    exercise_name = models.CharField(max_length=100)
    description = models.TextField(max_length=200)

class Routines(models.Model):
    routine_name = models.CharField(max_length=100)
    routine_description = models.TextField(max_length=200)
    exercises = models.ManyToManyField(Exercises)

class People(User):
    routines = models.ManyToManyField(Routines)

class ExerciseInRoutine(models.Model):
    exercise = models.ForeignKey(Exercises, on_delete=models.CASCADE)
    routine = models.ForeignKey(Routines, on_delete=models.CASCADE)
    default_sets = models.IntegerField()
    default_reps = models.IntegerField()


