from django.shortcuts import render, HttpResponse, redirect, reverse
from .models import User, Author, Book, Review
from django.contrib import messages
# Create your views here.
def dashboard(request):
    reviews = Review.objects.all().order_by('-id')[:5]
    books = Book.objects.all()
    context= {
        "reviews":reviews,
        "books": books
    }
    return render(request, 'book_review/dashboard.html', context)
def add(request):
    authors = Author.objects.all()
    context = {
        "authors": authors
    }
    return render(request, 'book_review/add_book.html', context)
def show_user(request, id):
    user = User.objects.get(id=id)
    user_reviews = user.user_review.all()
    count = user.user_review.count()
    context={
        "user":user,
        "count":count,
        "books": user_reviews
    }
    return render(request, "book_review/user_profile.html", context)
def show_book(request, id):
    book = Book.objects.get(id=id)
    reviews = book.book_review.all().order_by('-id')
    user = User.objects.get(id=request.session['id'])
    context= {
        "book":book,
        "reviews": reviews,
        "user": user
    }
    return render(request, 'book_review/book_profile.html', context)
def submitbook(request):
    submission = Review.objects.handle_submit(request.POST, request.session['id'])
    if 'error' in submission:
        messages.error(request, submission['error'])
        current_url = request.META['HTTP_REFERER']
        return redirect(current_url)
    if 'success' in submission:
        messages.success(request, submission['success'])
        bookpage = submission['review'].book.id
        return redirect(reverse('show_book', args = (bookpage,)))
def delete(request):
    delete = Review.objects.get(id=request.POST['delete']).delete()
    current_url = request.META['HTTP_REFERER']
    return redirect(current_url)
def logout(request):
    del request.session['login']
    del request.session['username']
    del request.session['id']
    request.session.modified = True
    return redirect('/')

def search(request):
    try:
        book_id = Book.objects.get(title__iexact=request.POST['booksearch'])
        return redirect(reverse('show_book', args = (book_id.id,)))
    except:
        book_id = Book.objects.get(title__iexact=request.POST['booksearch'])
        messages.error(request, "No book.")
        return redirect('/dashboard')
