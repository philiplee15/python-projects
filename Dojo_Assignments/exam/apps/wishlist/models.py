from django.db import models
from ..validation.models import User

class WishList(models.Model):
    user = models.OneToOneField(User)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class ItemManager(models.Manager):
    def validate_item(self, post, id):
        response = {}
        try:
            user = User.objects.get(id=id)
        except:
            response['error'] = "You must login to continue."
            return response
        if len(post['item']):
            if len(post['item']) < 3:
                response['error'] = "Item name must be at least 3 characteres."
                return response
            else:
                try:
                    Item.objects.get(name=post['item'])
                    response['error'] = "Item exists."
                    return response
                except:
                    try:
                        wish1 = WishList.objects.get(user=user)
                        item1 = Item.objects.create(name=post['item'], user=user)
                        item1.save()
                        item1.wishlist.add(wish1)
                        item1.save()
                        wish1.save()
                        response['success'] = "Item successfully created."
                        return response
                    except:
                        wish1 = WishList.objects.create(user=user)
                        wish1.save()
                        item1 = Item.objects.create(name=post['item'], user=user)
                        item1.save()
                        item1.wishlist.add(wish1)
                        item1.save()
                        wish1.save()
                        response['success'] = "Item successfully created."
                        return response
        else:
            response['error'] = "Please input item name."
            return response
    def addtomine(request, item, user):
        response = {}
        user = User.objects.get(id=user)
        item1 = Item.objects.get(name=item)
        try:
            wish1 = WishList.objects.get(user=user)
            item1.wishlist.add(wish1)
            response['success'] = "Item successfully added."
            return response
        except:
            wish1 = WishList.objects.create(user=user)
            wish1.save()
            item1.wishlist.add(wish1)
            response['success'] = "Item successfully created."
            return response

class Item(models.Model):
    name = models.CharField(max_length=200)
    user = models.ForeignKey(User)
    wishlist = models.ManyToManyField(WishList)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = ItemManager()
