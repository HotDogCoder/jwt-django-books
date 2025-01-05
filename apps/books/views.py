from pymongo import MongoClient
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi
from apps.books.presentation.controllers.book_controller import BookController
from apps.books.domain.models.book_model import BookModel
from rest_framework.permissions import IsAuthenticated
import json

from apps.books.serializers import BookSerializer



class BookListView(APIView):
    permission_classes = [IsAuthenticated]

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.controller = BookController()

    @swagger_auto_schema(
        operation_description="Retrieve a list of books with optional filters for title and author",
        manual_parameters=[
            openapi.Parameter(
                "title",
                openapi.IN_QUERY,
                description="Filter books by title",
                type=openapi.TYPE_STRING,
                required=False,
            ),
            openapi.Parameter(
                "author",
                openapi.IN_QUERY,
                description="Filter books by author",
                type=openapi.TYPE_STRING,
                required=False,
            ),
        ],
        responses={200: openapi.Response("Success")},
    )
    def get(self, request):
        # Extract filters from query parameters
        title = request.query_params.get('title')
        author = request.query_params.get('author')

        # Initialize BookModel and set filters if present
        book_model = BookModel()
        if title:
            book_model.title = title
        if author:
            book_model.author = author

        # If no filters were provided, return all records
        if not title and not author:
            # Pass an empty BookModel to fetch everything
            result = self.controller.query(BookModel())
        else:
            # Use the controller to query books with filters
            result = self.controller.query(book_model)

        # Serialize the data
        serializer = BookSerializer(result.data, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    @swagger_auto_schema(
        operation_description="Add a new book to the collection.",
        request_body=openapi.Schema(
            type=openapi.TYPE_OBJECT,
            properties={
                "title": openapi.Schema(type=openapi.TYPE_STRING, description="Title of the book"),
                "author": openapi.Schema(type=openapi.TYPE_STRING, description="Author of the book"),
                "published_date": openapi.Schema(
                    type=openapi.TYPE_STRING,
                    format="date",
                    description="Published date of the book in YYYY-MM-DD format"
                ),
                "genre": openapi.Schema(type=openapi.TYPE_STRING, description="Genre of the book"),
                "price": openapi.Schema(type=openapi.TYPE_NUMBER, description="Price of the book"),
            },
            required=["title", "author", "published_date", "price"],  # Mark required fields
        ),
        responses={
            201: openapi.Response(
                description="Book created successfully.",
                schema=openapi.Schema(
                    type=openapi.TYPE_OBJECT,
                    properties={
                        "_id": openapi.Schema(type=openapi.TYPE_STRING, description="ID of the book"),
                    },
                    example={"_id": "64a7f3d1234567890abcdef0"}
                ),
            ),
            400: openapi.Response(
                description="Validation error",
                schema=openapi.Schema(
                    type=openapi.TYPE_OBJECT,
                    properties={
                        "error": openapi.Schema(type=openapi.TYPE_STRING, description="Error message"),
                    },
                    example={"error": "Missing required field: title"},
                ),
            ),
        },
    )
    def post(self, request):
        try:
            # Parse the JSON data
            book_data = json.loads(request.body)

            # Initialize a new BookModel and set attributes
            book_model = BookModel()
            book_model.title = book_data.get("title", "")
            book_model.author = book_data.get("author", "")
            book_model.published_date = book_data.get("published_date", "")
            book_model.genre = book_data.get("genre", "")
            book_model.price = book_data.get("price", "")

            # Use the controller to create a new book
            result = self.controller.post(book_model)

            # Return a success response
            return Response(result.data, status=status.HTTP_201_CREATED)
        except KeyError as e:
            return Response({"error": f"Missing required field: {str(e)}"}, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

class BookDetailView(APIView):
    permission_classes = [IsAuthenticated]

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.controller = BookController()

    @swagger_auto_schema(
        operation_description="Retrieve a specific book by ID",
        manual_parameters=[
            openapi.Parameter(
                "book_id",
                openapi.IN_PATH,
                description="ID of the book",
                type=openapi.TYPE_STRING,
                required=True,
            )
        ],
        responses={200: openapi.Response("Success")},
    )
    def get(self, request, book_id):
        book_model = BookModel()
        book_model._id = book_id
        result = self.controller.get(book_model)
        serializer = BookSerializer(result.data)
        return Response(serializer.data, status=status.HTTP_200_OK)

    @swagger_auto_schema(
        operation_description="Update an existing book",
        request_body=openapi.Schema(
            type=openapi.TYPE_OBJECT,
            properties={
                "title": openapi.Schema(type=openapi.TYPE_STRING, description="Title of the book"),
                "author": openapi.Schema(type=openapi.TYPE_STRING, description="Author of the book"),
                "published_date": openapi.Schema(
                    type=openapi.TYPE_STRING,
                    format="date",
                    description="Publication date of the book in YYYY-MM-DD format"
                ),
                "genre": openapi.Schema(type=openapi.TYPE_STRING, description="Genre of the book"),
                "price": openapi.Schema(type=openapi.TYPE_NUMBER, description="Price of the book"),
            },
            required=["title", "author"],  # Define required fields
        ),
        manual_parameters=[
            openapi.Parameter(
                "book_id",
                openapi.IN_PATH,
                description="ID of the book to update",
                type=openapi.TYPE_STRING,
                required=True,
            )
        ],
        responses={
            200: openapi.Response(
                description="Book updated successfully",
                schema=openapi.Schema(
                    type=openapi.TYPE_OBJECT,
                    properties={
                        "modified_count": openapi.Schema(
                            type=openapi.TYPE_INTEGER,
                            description="Number of documents modified"
                        ),
                    },
                    example={"modified_count": 1},
                ),
            ),
            404: openapi.Response(
                description="Book not found",
                schema=openapi.Schema(
                    type=openapi.TYPE_OBJECT,
                    properties={
                        "error": openapi.Schema(type=openapi.TYPE_STRING, description="Error message"),
                    },
                    example={"error": "Book not found."},
                ),
            ),
            400: openapi.Response(
                description="Validation error",
                schema=openapi.Schema(
                    type=openapi.TYPE_OBJECT,
                    properties={
                        "error": openapi.Schema(type=openapi.TYPE_STRING, description="Error message"),
                    },
                    example={"error": "Invalid input data."},
                ),
            ),
        },
    )
    def put(self, request, book_id):
        book_data = json.loads(request.body)
        book_model = BookModel(_id=book_id, **book_data)
        result = self.controller.put(book_model)
        return Response(result.data, status=status.HTTP_200_OK)

    @swagger_auto_schema(
        operation_description="Delete a book by ID",
        manual_parameters=[
            openapi.Parameter(
                "book_id",
                openapi.IN_PATH,
                description="ID of the book to delete",
                type=openapi.TYPE_STRING,
                required=True,
            )
        ],
        responses={204: openapi.Response("Deleted")},
    )
    def delete(self, request, book_id):
        book_model = BookModel(_id=book_id)
        result = self.controller.delete(book_model)
        return Response(result.data, status=status.HTTP_204_NO_CONTENT)

class AveragePriceView(APIView):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        # Use the existing repository
        self.controller = BookController()

    @swagger_auto_schema(
        operation_description="Retrieve the average price of books published in a specific year.",
        manual_parameters=[
            openapi.Parameter(
                name="year",
                in_=openapi.IN_PATH,
                description="Year of publication to calculate the average price",
                type=openapi.TYPE_INTEGER,
                required=True,
            )
        ],
        responses={
            200: openapi.Response(
                description="Success",
                schema=openapi.Schema(
                    type=openapi.TYPE_OBJECT,
                    properties={
                        "year": openapi.Schema(type=openapi.TYPE_INTEGER, description="The year"),
                        "average_price": openapi.Schema(
                            type=openapi.TYPE_NUMBER, description="The average price of books"
                        ),
                    },
                    example={"year": 2023, "average_price": 17.5},
                ),
            ),
            404: openapi.Response(
                description="No books found for the specified year",
                schema=openapi.Schema(
                    type=openapi.TYPE_OBJECT,
                    properties={
                        "message": openapi.Schema(type=openapi.TYPE_STRING, description="Error message"),
                    },
                    example={"message": "No books found for the year 2023."},
                ),
            ),
            500: openapi.Response(
                description="Internal server error",
                schema=openapi.Schema(
                    type=openapi.TYPE_OBJECT,
                    properties={
                        "error": openapi.Schema(type=openapi.TYPE_STRING, description="Error message"),
                    },
                    example={"error": "Failed to calculate average price"},
                ),
            ),
        },
    )
    def get(self, request, year):
        try:
            # Call the repository method
            average_price = self.controller.get_average_price_by_year(year)

            if average_price is None:
                return Response(
                    {"message": f"No books found for the year {year}."},
                    status=status.HTTP_404_NOT_FOUND,
                )

            return Response({"year": year, "average_price": average_price}, status=status.HTTP_200_OK)

        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
