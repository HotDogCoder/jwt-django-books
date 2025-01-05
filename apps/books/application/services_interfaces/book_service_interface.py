from abc import ABC, abstractmethod
from apps.books.domain.models.book_model import BookModel

class BookServiceInterface(ABC):
    def __init__(self):
        super().__init__()


    @abstractmethod
    def query(self, book_model: BookModel):
        return book_model
    @abstractmethod
    def upload(self, book_model: BookModel):
        return book_model
    @abstractmethod
    def post(self, book_model: BookModel):
        return book_model
    @abstractmethod
    def get(self, book_model: BookModel):
        return book_model
    @abstractmethod
    def put(self, book_model: BookModel):
        return book_model
    @abstractmethod
    def delete(self, book_model: BookModel):
        return book_model
