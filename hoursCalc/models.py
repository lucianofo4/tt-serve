from django.db import models
import datetime
from django.shortcuts import render, get_object_or_404
from django.contrib.auth.models import User


class Shift(models.Model):
    name = models.ForeignKey(User, on_delete=models.CASCADE)
    clock_in = models.DateTimeField(
        blank=True, null=True)  
    clock_out = models.DateTimeField(
        blank=True, null=True)  
    date = models.DateField(blank=True, null=True)  # não branco ou nulo
    description = models.TextField(blank=True, null=True, max_length=600)

    class Meta:
        ordering = ['-date']

    def __str__(self):
        return str(self.name)

    def save(self, *args, **kwargs):
        
        super(Shift, self).save(*args, **kwargs)
