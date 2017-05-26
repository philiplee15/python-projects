from django.db import models
import re

# Create your models here.
class UserManager(models.Manager):
    def validate(self, post):
        EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
        UNAME_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]{0,16}$')
        PW_REGEX = re.compile(r'^[A-Z](?=.+?[a-z])(?=.+?[0-9])(?=.+?[.!@#$%^&*()_+]).{5,19}$')
        response = {
            "error": []
        }
        try:
            emailquery = User.userManager.get(email = post['email'])
            response['error'].append('E-mail already exists.')
        except:
            pass
        try:
            uquery = User.userManager.get(username = post['username'])
            response['error'].append('E-mail already exists.')
        except:
            pass
        if len(post['fname']) < 2 or len(post['lname']) < 2:
            response['error'].append('Name too short.')
        if not EMAIL_REGEX.match(post['email']):
            response['error'].append('Email invalid.')
        if not UNAME_REGEX.match(post['username']):
            response['error'].append('Username invalid.')
        if not PW_REGEX.match(post['password']):
            response['error'].append('Password invalid. \n -Must be at least 5 characters. \n -First letter must be capital. \n -Must contain at least 1 special characters.')
        if post['password'] != post['confirm']:
            response['error'].append('Passwords do not match.')
        if not post['bday']:
            response['error'].append('Please input a birthday.')
        else:
            print(post['bday'])
        if not response['error']:
            response['success'] = "You have successfully registered. Please login to begin your journey."
            user = User.userManager.create(first_name=post['fname'], last_name=post['lname'], username=post['username'], password=post['password'], bday=post['bday'])
            return response
        else:
            return response


class User(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.CharField(max_length=50)
    username = models.CharField(max_length=30)
    password = models.CharField(max_length=30)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = UserManager()

class Secret(models.Model):
    text = models.CharField(max_length=30)
    user = models.ForeignKey(User, related_name="secrets")
    anon = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
class Like(models.Model):
    status = models.BooleanField(default="False")
    secret = models.ForeignKey(Secret, related_name="secret_like")
    user = models.ForeignKey(User, related_name="user_like")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
