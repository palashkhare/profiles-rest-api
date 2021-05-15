from rest_framework import serializers

class HelloSerializer(serializers.Serializer):
    """Serializer to test Post function in API views
        Serializers are function which are used to convert post data into database
        objects.
        They work similar to Django forms
    """
    name = serializers.CharField(max_length=10)
