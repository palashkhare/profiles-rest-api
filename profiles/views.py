from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from profiles import serializers

class HelloApiView(APIView):
    """Test API View"""

    # serializer_class variable tells django about which serializer to be used
    serializer_class = serializers.HelloSerializer

    def get(self, request, format=None):
        """Returns a list of APIView features
            Request is http request object
            format : if API format is enabled. In test example we are not using
            but as a best practice this should be kept in place if in future we
            enable formating
        """
        # example features
        an_apiview = [
            'Uses HTTP methods as function )get, put, patch, post, delete',
            'It is similar to traditional Django views',
            'Gives you most control over your applcation logic',
            'Is mapped manually to URLs',
        ]

        return Response({'message' : 'Hello', 'an_apiview': an_apiview})

    def post(self, request):
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            name = serializer.validated_data.get('name')
            message = f'hello {name}'
            return Response({'message':message})
        else:
            return Response(
                serializer.errors,
                status=status.HTTP_400_BAD_REQUEST
                )

    def put(self, request, pk=None):
        """Update an object
        Put command is used to completely update an object.
        PK is the primary key which is provided in the uRL to process Put
        """
        return Response({'method':'Put'})

    def patch(self, request, pk=None):
        """Update an object partially
        Patch command is used to partially update an object.
        PK is the primary key which is provided in the uRL to process Patch
        """
        return Response({'method':'Patch'})

    def delete(self, request, pk=None):
        """Delete an object"""
        return Response({'method':'delete'})
