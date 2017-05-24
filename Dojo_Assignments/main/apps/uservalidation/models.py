from django.db import models


# Create your models here.
class UserManager(models.Manager):
    def login(self, username, password):
        print("If succcessful pass user info dict")
        print("If unsuccessful return error dict")
        return("I will be a future login method.")
    def register(self, **kwargs):
        pass

class User(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    username = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    password = models.CharField(max_length=50)
    bday = models.DateField(auto_now=False, auto_now_add=False)

    userManager = UserManager()
