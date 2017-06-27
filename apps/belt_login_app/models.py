from __future__ import unicode_literals

from django.db import models
from django.contrib import messages
# from django.db.models import Model
import bcrypt
import re


EMAIL_REGEX = re.compile (r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
NAME_REGEX = re.compile(r'^[a-zA-Z ]+$')
# Create your models here.
class UserManager(models.Manager):
    def isValidRegistration(self, postData):
        user_objects = {'status' : True, 'errors' : [], 'user' : None}
        print postData, '*'*50

        if len(postData['name']) < 3:
            user_objects['status'] = False
            user_objects['errors'].append('name minimum length: 3')

        if not postData['name'].isalpha():
            user_objects['status'] = False
            user_objects['errors'].append('name must contain only letters')
            print postData['name']

        if len(postData['username']) < 3:
            user_objects['status'] = False
            user_objects['errors'].append('username minimum length: 3')

        if not postData['username'].isalpha():
            user_objects['status'] = False
            user_objects['errors'].append('username must contain only letters')

        if len(postData['password']) < 8:
            user_objects['status'] = False
            user_objects['errors'].append('password minimum length: 8')

        # if not EMAIL_REGEX.match(postData['email']):
        #     user_objects['status'] = False
        #     user_objects['errors'].append('please enter a valid email')

        if postData['password'] != postData['pass_confirm']:
            user_objects['status'] = False
            user_objects['errors'].append('password did not match')
            if User.objects.filter(email = postData['email']):
                user_objects['status'] = False
		user_objects['errors'].append("this email is already registered, login instead")

        if user_objects['status'] == True:
            #messages.success(request, "hello. you are registered!")
            hashed = bcrypt.hashpw(postData['password'].encode(), bcrypt.gensalt())
            User.objects.create(name = postData['name'], username = postData['username'], password = hashed)

        return user_objects


    def UserExistsLogin(self, postData):
        user_objects = {'status' : True, 'errors' : [], 'user' : None}
        user_objects['status'] = True

        if User.objects.filter(username = postData['username']):

            hashed = User.objects.get(username = postData['username']).password
            hashed = hashed.encode('utf-8')
            password = postData['password']
            password = password.encode('utf-8')

            if bcrypt.hashpw(password, hashed) == hashed:
                #messages.success(request, "hello!")
                user_objects['status'] = True
                #user = User.objects.get(email )

            else:

                user_objects['errors'].append("sorry, somthing went wrong. try email and password again.")
                user_objects['status'] = False

        else:

            user_objects['errors'].append("sorry, somthing went wrong. try email and password again.")
            user_objects['status'] = False

        return user_objects

class User(models.Model):
    name = models.CharField(max_length=50)
    username = models.CharField(max_length=50)
    # email = models.EmailField()
    password = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    userManager = UserManager()
    objects = UserManager()
