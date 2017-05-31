from django.db import models
import re
import bcrypt

class UserManager(models.Manager):
    def validate_registration(self, post):
        response = {
            "error": []
        }
        try:
            uquery = User.objects.get(username = post['username'])
            response['error'].append('Username already exists.')
        except:
            pass
        if len(post['name']) < 3:
            response['error'].append('Name too short.')
        if len(post['username']) < 3:
            response['error'].append('Username too short.')
        if len(post['password']) < 8:
            response['error'].append('Password must be 8 chars.')
        if post['password'] != post['confirm']:
            response['error'].append('Passwords do not match.')
        if not post['hired']:
            response['error'].append('Please input a hire date.')
        if not response['error']:
            response['success'] = "Registration complete. Login to post."
            hashed = bcrypt.hashpw(post['password'].encode('UTF-8'), bcrypt.gensalt())
            user = User.objects.create(name=post['name'], username=post['username'], password=hashed, hired=post['hired'])
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
    name = models.CharField(max_length=30)
    username = models.CharField(max_length=30)
    password = models.CharField(max_length=30)
    hired = models.DateField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = UserManager()
