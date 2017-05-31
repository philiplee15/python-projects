from django.db import models
import re
import bcrypt

class UserManager(models.Manager):
    def validate_registration(self, post):
        EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
        UNAME_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]{0,16}$')
        PW_REGEX = re.compile(r'^[A-Z](?=.+?[a-z])(?=.+?[0-9])(?=.+?[.!@#$%^&*()_+]).{5,19}$')
        response = {
            "error": []
        }
        try:
            emailquery = User.objects.get(email = post['email'])
            response['error'].append('E-mail already exists.')
        except:
            pass
        try:
            uquery = User.objects.get(username = post['username'])
            response['error'].append('Username already exists.')
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
            response['success'] = "Registration complete. Login to post."
            hashed = bcrypt.hashpw(post['password'].encode('UTF-8'), bcrypt.gensalt())
            user = User.objects.create(first_name=post['fname'], last_name=post['lname'], username=post['username'], email=post['email'], password=hashed)
            return response
        else:
            return response

    def validate_login(self, user, pw):
        response = {}
        print(user, pw)
        try:
            user = User.objects.get(username=user)
        except:
            response['error'] = "Username wrong."
            return response
        hashed2 = bcrypt.hashpw(pw.encode('UTF-8'), user.password.encode('UTF-8')).decode('UTF-8')
        if hashed2 == user.password:
            response['success'] = "Login successful."
        else:
            response['error'] = "Password invalid."
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
