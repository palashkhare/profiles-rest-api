from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import viewsets
from rest_framework.authentication import TokenAuthentication
from rest_framework import filters
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.settings import api_settings
# IsAuthenticatedOrReadOnly : This permission allows user to readall the feeds
# nut modify the feed only which they are authenticated for
# IsAuthenticated: This to restrict users from watching anything if they are
# not  authenticated
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated
from profiles import serializers
from profiles import models
from profiles import permissions


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


class HelloViewSets(viewsets.ViewSet):
    """Test API Viewset
        This is used when CRUD operations are performed
    """
    serializer_class = serializers.HelloSerializer
    def list(self, request):
        """Get Request: Return a list"""
        a_viewset = [
            'Uses actions (list, create, update, retrieve, update, partial_update)',
            'Automatically maps to the urls using Routers',
            'Provides more functionality with less code',
        ]

        return Response({'message': "Hello", 'a_viewset':a_viewset})

    def create(self, request):
        """POST: create a new hello meaasge"""
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            name = serializer.validated_data.get('name')
            message = f'Hello {name}'
            return Response({'message' : message})
        else:
            return Response(
                serializer.error,
                status=status.HTTP_400_BAD_REQUEST
            )

    def retrieve(self, request, pk=None):
        """Handle GET request by ID"""
        return Response({'http_method':'GET'})

    def update(self, request, pk=None):
        """Handle PUT request by ID"""
        return Response({'http_method':'PUT'})


    def partial_update(self, request, pk=None):
        """Handle PATCH request by ID"""
        return Response({'http_method':'PATCH'})


    def destroy(self, request, pk=None):
        """Handle DELETE request by ID"""
        return Response({'http_method':'DELETE'})

class UserProfileViewSet(viewsets.ModelViewSet):
    """ handel creating and updating profiles
        Modelviewset set are a type of regular viewset but they are made to
        perform model based operations.

        ModelViewSet by default knows that Create, Update, Read and Delete
        operations
    """
    serializer_class = serializers.UserProfileSerializer
    queryset = models.UserProfile.objects.all()
    authentication_classes = (TokenAuthentication,)
    permission_classes = (permissions.UpdateOwnProfile, )
    filter_backends = (filters.SearchFilter,)
    search_fields = ('name', 'email')


class UserLoginApiView(ObtainAuthToken):
    """ Handle Creating User Auth tokens """
    renderer_classes = api_settings.DEFAULT_RENDERER_CLASSES

class UserProfileFeedViewSet(viewsets.ModelViewSet):
    """Creating, reading and updation profile feed items """
    authentication_classes = (TokenAuthentication,)
    serializer_class = serializers.ProfileFeedItemSerializer
    queryset = models.ProfileFeedItems.objects.all() # This mean we will be managing all the items in model
    permission_classes = (
        permissions.UpdateOwnStatus,
        IsAuthenticated,
    )
    def perform_create(self, serializer):
        """ Sets the user profile to the loggedin user
            Overrides behaviour of object creation from model viewset.
            When a request is made through ModelViewSet it is passed into
            Serializer class and validated and then passed into .save function
            To customize the logic for object creation, perform_create function
            can be used.
        """
        print("*"*8, self.request, self.request.user)
        serializer.save(user_profile=self.request.user)
