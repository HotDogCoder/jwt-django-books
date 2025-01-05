from apps.books.application.services_interfaces.book_service_interface import BookServiceInterface
from apps.books.infrastructure.repositories.book_repository import BookRepository
from apps.books.domain.models.book_model import BookModel

class BookService(BookServiceInterface):
    def __init__(self):
        super().__init__()
        self.book_repository = BookRepository()

    def query(self, book_model: BookModel):
        return self.book_repository.query(book_model)
    def upload(self, book_model: BookModel):
        return self.book_repository.upload(book_model)
    def post(self, book_model: BookModel):
        return self.book_repository.post(book_model)
    def get(self, book_model: BookModel):
        return self.book_repository.get(book_model)
    def put(self, book_model: BookModel):
        return self.book_repository.put(book_model)
    def delete(self, book_model: BookModel):
        return self.book_repository.delete(book_model)
    def get_average_price_by_year(self, year: int):
        return self.book_repository.get_average_price_by_year(year)
