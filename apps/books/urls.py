from django.urls import path
from .views import AveragePriceView, BookListView, BookDetailView

urlpatterns = [
    path('', BookListView.as_view(), name='book-list'),  # GET /api/books/, POST /api/books/
    path('<str:book_id>/', BookDetailView.as_view(), name='book-detail'),  # GET, PUT, DELETE /api/books/{book_id}/
    path("average-price/<int:year>/", AveragePriceView.as_view(), name="average_price"),

]
