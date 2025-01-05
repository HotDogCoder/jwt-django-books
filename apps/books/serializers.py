from rest_framework import serializers

class BookSerializer(serializers.Serializer):
    _id = serializers.CharField()
    title = serializers.CharField()
    author = serializers.CharField()
    published_date = serializers.DateField()
    genre = serializers.CharField()
    price = serializers.DecimalField(max_digits=10, decimal_places=2)
