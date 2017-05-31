from django.db import models
from ..validation.models import User
# Create your models here.

class Author(models.Model):
    name = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
class Book(models.Model):
    title = models.CharField(max_length=100)
    author = models.ForeignKey(Author, related_name="author_book")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class ReviewManager(models.Manager):
    def handle_submit(self, post, user_id):
        response = {}
        try:
            user = User.objects.get(id=user_id)
        except:
            response['error'] = "Please re-log to continue."
            return response
        if post['title']:
            try:
                book_title = Book.objects.get(title=post['title'])
            except:
                if post['authors'] != "None":
                    author_name = post['authors']
                else:
                    if post['author']:
                        try:
                            author_name = Author.objects.get(name=post['author'])
                        except:
                            author_name = Author.objects.create(name=post['author'])
                    else:
                        response['error']= "Please input author name."
                        return response
                book_title = Book.objects.create(title=post['title'], author=author_name)
        else:
            response['error'] = "Please input book name."
            return response
        if post['review']:
            review = Review.objects.create(content=post['review'], rating=post['rating'], user=user, book=book_title)
            response['success'] = "Your review has successfully posted."
            response['review'] = review
            return response
        else:
            response['error'] = "Please write your review."
            return response

class Review(models.Model):
    content = models.CharField(max_length=500)
    rating = models.IntegerField()
    user = models.ForeignKey(User, related_name ="user_review")
    book = models.ForeignKey(Book, related_name="book_review")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = ReviewManager()
