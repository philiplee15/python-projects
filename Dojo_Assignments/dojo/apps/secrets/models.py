from django.db import models
import re
import bcrypt

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
    def verify(self, post):
        response = {}
        try:
            user = User.objects.get(username=post['user'])
        except:
            response['error'] = "Username wrong."
            return response
        hashed2 = bcrypt.hashpw(post['pass'].encode('UTF-8'), user.password.encode('UTF-8')).decode('UTF-8')
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

class SecretManager(models.Manager):
    def validate_secret(self, post, id):
        response = {}
        theuser = User.objects.get(id=id)
        if 'anon' in post:
            boo = True
        else:
            boo = False
        if post['comment']:
            s = Secret.objects.create(text=post['comment'], user=theuser, anon=boo)
            response['success'] = "Your post has been submitted, {}.".format(s.user.first_name)
            return response
        else:
            response['error'] = "We didn't hear any whispers."
            return response
    def count_likes(self):
        secret_like_set = Secret.secret_like
        count = 0
        for val in secret_like_set:
            count+=1
        return count
class Secret(models.Model):
    text = models.CharField(max_length=30)
    user = models.ForeignKey(User, related_name="secrets")
    anon = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = SecretManager()
    def like_count(self):
        return Like.objects.filter(secret=self).count()
    def like_owners(self):
        return list(self.secret_like.all().values_list('user_id', flat=True))    
class Like(models.Model):
    secret = models.ForeignKey(Secret, related_name="secret_like")
    user = models.ForeignKey(User, related_name="user_like")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
