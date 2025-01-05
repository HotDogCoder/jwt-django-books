from django.db import models
from djongo import models

class Book(models.Model):
    """
    ORM Model for Book using MongoDB's native `_id` as the primary key.
    """
    _id = models.ObjectIdField(primary_key=True)  # Use MongoDB's native `_id`
    title = models.CharField(max_length=255, help_text="Title of the book")
    author = models.CharField(max_length=255, help_text="Author of the book")
    published_date = models.DateField(help_text="Published date of the book")
    genre = models.CharField(max_length=100, help_text="Genre of the book")
    price = models.DecimalField(max_digits=10, decimal_places=2, help_text="Price of the book")

    class Meta:
        db_table = "books"

    def __str__(self):
        return self.title
