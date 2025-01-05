class BookModel:
    def __init__(self, _id = '', title = '', author = '', published_date = '', genre = '', price = ''):
        # title, author, published_date, genre, price.
        self._id = _id
        self.title = title
        self.author = author
        self.published_date = published_date
        self.genre = genre
        self.price = price
        self.data = None

        pass

    def dict(self):
        return {
            '_id': self._id,
            'title': self.title,
            'author': self.author,
            'published_date': self.published_date,
            'genre': self.genre,
            'price': self.price,
            'data': self.data
        }
