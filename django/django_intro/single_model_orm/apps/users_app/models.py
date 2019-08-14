from django.db import models

class User(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email_address = models.CharField(max_length=255)
    age = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

# ONE TO MANY RELATIONSHIP
# class Author(models.Model):
#     name = models.CharField(max_length=255)
#     created_at = models.DateTimeField(auto_now_add=True)
#     updated_at = models.DateTimeField(auto_now=True)
# class Book(models.Model):
#     title = models.CharField(max_length=255)
#     author = models.ForeignKey(Author, related_name="books")
#     created_at = models.DateTimeField(auto_now_add=True)
#     updated_at = models.DateTimeField(auto_now=True)
# my_book = Book.objects.create(title="Little Women", author=Author.objects.get(id=2))

# <h1>Author List</h1>
# <ul>
#   {% for author in authors %}
#     <li>{{author.name}}
#       <ul>
#     	<!-- looping through each author's books! -->
#         {% for book in author.books.all %}	
#           <li><em>{{book.title}}</em></li>
#         {% endfor %}
#       </ul>
#     </li>
#   {% endfor %}
# </ul>