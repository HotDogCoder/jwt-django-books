import os
from pymongo import MongoClient
from apps.books.application.repositories_interfaces.book_repository_interface import BookRepositoryInterface
from apps.books.domain.models.book_model import BookModel
from bson.objectid import ObjectId

class BookRepository(BookRepositoryInterface):
    def __init__(self):
        super().__init__()
        # Configure your MongoDB connection using environment variables
        db_user = os.environ.get('DB_MONGO_USER')
        db_password = os.environ.get('DB_MONGO_PASSWORD')
        db_host = f"mongodb+srv://{db_user}:{db_password}@cluster0.ml6w3.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"
        
        # Initialize MongoDB client
        self.client = MongoClient(db_host)
        self.db = self.client["db_books"]  # Use the 'NAME' from the config
        self.collection = self.db["books"]  # Collection name

    def query(self, book_model: BookModel):
        # Use filter criteria from the book model
        filter_criteria = {}
        if book_model.title:
            filter_criteria["title"] = book_model.title
        if book_model.author:
            filter_criteria["author"] = book_model.author
        results = list(self.collection.find(filter_criteria))
        # Store the results in book_model.data
        book_model.data = results
        return book_model

    def upload(self, book_model: BookModel):
        # Convert the book model's data to a list of dictionaries
        book_data = book_model.data if isinstance(book_model.data, list) else []
        result = self.collection.insert_many(book_data)
        # Store the inserted IDs in book_model.data
        book_model.data = list(map(str, result.inserted_ids))
        return book_model

    def post(self, book_model: BookModel):
        # Convert the book model's data to a dictionary
        book_data = book_model.dict()

        if "_id" in book_data:
            del book_data["_id"]

        result = self.collection.insert_one(book_data)
        # Store the inserted ID in book_model.data
        book_model.data = str(result.inserted_id)
        return book_model

    def get(self, book_model: BookModel):
        # Retrieve a single book by its ID
        book_id = book_model._id  # Assume `id` is a property of `BookModel`
        result = self.collection.find_one({"_id": ObjectId(book_id)})
        # Store the result in book_model.data
        book_model.data = result
        return book_model

    def put(self, book_model: BookModel):
        # Extract the book ID
        book_id = book_model._id  # Assume `_id` is a property of `BookModel`

        # Convert the book model's data to a dictionary
        update_data = book_model.dict()

        # Remove the `_id` field from the update data
        if "_id" in update_data:
            del update_data["_id"]

        if "data" in update_data:
            del update_data["data"]

        # Perform the update operation
        result = self.collection.update_one(
            {"_id": ObjectId(book_id)},  # Match document by `_id`
            {"$set": update_data}        # Update fields except `_id`
        )

        # Store the modified count in book_model.data
        book_model.data = {"modified_count": result.modified_count}
        return book_model

    def delete(self, book_model: BookModel):
        # Delete a book by its ID
        book_id = book_model._id  # Assume `id` is a property of `BookModel`
        result = self.collection.delete_one({"_id": ObjectId(book_id)})
        # Store the deleted count in book_model.data
        book_model.data = {"deleted_count": result.deleted_count}
        return book_model

    def get_average_price_by_year(self, year: int):
        """
        Calculate the average price of books published in a specific year.
        """
        try:
            # MongoDB aggregation pipeline
            pipeline = [
                {"$match": {"published_date": {"$regex": f"^{year}"}}},  # Match by year
                {
                    "$group": {
                        "_id": None,  # Grouping key, None since we want an overall average
                        "average_price": {"$avg": "$price"},  # Calculate average price
                    }
                },
                {"$project": {"_id": 0, "average_price": 1}},  # Remove `_id` from results
            ]

            # Execute the pipeline
            result = list(self.collection.aggregate(pipeline))

            # Return the average price if available
            if result:
                return result[0]["average_price"]
            return None
        except Exception as e:
            raise ValueError(f"Failed to calculate average price: {str(e)}")
