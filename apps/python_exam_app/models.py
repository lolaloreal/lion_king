from __future__ import unicode_literals

from django.db import models
import datetime

# Create your models here.
class TripManager(models.Manager):
    print 'i am the manager'
    def add(self, postData):
        results = {'status' : True, 'errors' : []}
        if not postData['destination'] or len(postData['destination']) < 1:
            results['status'] = False
            results['errors'].append('destination is invalid | cannot leave blank')
        if not postData['plan'] or len(postData['plan']) < 1:
            results['status'] = False
            results['errors'].append('plan is invalid | cannot leave blank')
        if not postData['start_date'] or len(postData['start_date']) < 1: #or postData['start_date'] #< datetime.datetime.today():
            results['status'] = False
            results['errors'].append('date is invalid | cannot leave blank | must be in the future')
        if not postData['end_date'] or len(postData['end_date']) < 1: #or postData['end_date'] < datetime.date.today() or postData['end_date'] < postData['start_date']:
            results['status'] = False
            results['errors'].append('date is invalid | cannot leave blank | must after departure date')
        if results['status'] == True:
            trip = Trip.objects.create(destination=postData['destination'], plan=postData['plan'], start_date=postData['start_date'], end_date=postData['end_date'])
            trip.save()
        return results



class Trip(models.Model):
    destination = models.CharField(max_length=200)
    plan = models.CharField(max_length=200)
    start_date = models.DateTimeField(datetime.date.today)
    end_date = models.DateTimeField(datetime.date.today)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    print 'trip model loaded'
    objects = TripManager()
