from apps.books.application.services.book_service import BookService
from apps.books.domain.models.book_model import BookModel

class BookController:
    def __init__(self):
        super().__init__()
        self.book_service = BookService()

    def query(self, book_model: BookModel):
        return self.book_service.query(book_model)
    def upload(self, book_model: BookModel):
        return self.book_service.upload(book_model)
    def post(self, book_model: BookModel):
        return self.book_service.post(book_model)
    def get(self, book_model: BookModel):
        return self.book_service.get(book_model)
    def put(self, book_model: BookModel):
        return self.book_service.put(book_model)
    def delete(self, book_model: BookModel):
        return self.book_service.delete(book_model)
    def get_average_price_by_year(self, year: int):
        return self.book_service.get_average_price_by_year(year)
