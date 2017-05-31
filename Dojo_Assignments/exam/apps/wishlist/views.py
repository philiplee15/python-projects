from django.shortcuts import render, HttpResponse, redirect, reverse
from .models import User, Item, WishList
from django.contrib import messages

# Create your views here.
def dashboard(request):
    if 'id' not in request.session:
        return redirect('/')
    user = User.objects.get(id=request.session['id'])
    try:
        user_wishes = WishList.objects.get(user=user)
        items_on_list = Item.objects.filter(wishlist=user_wishes).order_by("-updated_at")
        other_items = Item.objects.all().exclude(wishlist=user_wishes)
        context = {
            "wishlist": items_on_list,
            "other":other_items
        }
    except:
        other_items = Item.objects.all().exclude(user=user)
        context = {
            "other":other_items
        }
        return render(request, "wishlist/dashboard.html", context)
    return render(request, "wishlist/dashboard.html", context)
def show_item(request, id):
    item_name = Item.objects.get(id=id)
    item_users = item_name.wishlist
    print(item_users)
    context = {
        "item": item_name,
        "users": item_users
    }
    return render(request, "wishlist/item_profile.html", context)
def create(request):
    return render(request, "wishlist/create.html")
def validate_item(request):
    new_item = Item.objects.validate_item(request.POST, request.session['id'])
    if 'error' in new_item:
        messages.error(request, new_item['error'])
        return redirect('/wish_items/create')
    if 'success' in new_item:
        return redirect('/dashboard')
    return redirect('/dashboard')

def addtomy(request):
    addtomylist = Item.objects.addtomine(request.POST['item'], request.session['id'])
    return redirect('/dashboard')
def delete(request):
    user = User.objects.get(id=request.session['id'])
    if 'remove' in request.POST:
        wish1 = WishList.objects.get(user=user)
        item1 = Item.objects.get(id=request.POST['item_id'])
        item1.wishlist.remove(wish1)
        item1.save()
        wish1.save()
        return redirect('/dashboard')
    if 'delete' in request.POST:
        item1 = Item.objects.get(id=request.POST['item_id']).delete()
        return redirect('/dashboard')

def search(request):
    try:
        item_id = Item.objects.get(name__iexact=request.POST['itemsearch'])
        return redirect(reverse('show_item', args = (item_id.id,)))
    except:
        messages.error(request, "No book.")
        return redirect('/dashboard')
def logout(request):
    del request.session['login']
    del request.session['username']
    del request.session['id']
    request.session.modified = True
    return redirect('/')
