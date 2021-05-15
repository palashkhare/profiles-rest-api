from rest_framework.views import APIView
from rest_framework.response import Response


class HelloApiView(APIView):
    """Test API View"""

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
