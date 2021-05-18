from rest_framework import serializers

from profiles import models


class HelloSerializer(serializers.Serializer):
    """Serializer to test Post function in API views
        Serializers are function which are used to convert post data into database
        objects.
        They work similar to Django forms
    """
    name = serializers.CharField(max_length=10)

class UserProfileSerializer(serializers.ModelSerializer):
    """Create a serializer for user Profile model.
        To derive a serializer from DB model, a Meta class needs to be defined.
        called 'Model Serializer'
        Fields  which we want to be accessible are defined in fields variable
    """

    class Meta:
        model = models.UserProfile
        # fields variable defines which fields of model can be accessed by serializer
        fields = ('id', 'email', 'name', 'password', 'is_superuser')
        # extra_kwargs is defined to create rules for particular feilds defined
        # in fields variable
        extra_kwargs = {
            'password' : {
                'write_only' : True,
                'style' : {'input_type': 'password'}
            },
            'is_superuser' : {
                'read_only' : True
            }
        }

    def create(self, validated_data):
        """Create and return new user
            This function will override the create function in of Serializer
        """

        user = models.UserProfile.objects.create_user(
            email=validated_data['email'],
            name=validated_data['name'],
            password=validated_data['password']
        )

        return user

class ProfileFeedItemSerializer(serializers.ModelSerializer):
    """ModelSerializer for feed"""

    class Meta:
        model = models.ProfileFeedItems
        fields = ('id', 'user_profile', 'status_text', 'created_on')

        extra_kwargs = {
            'user_profile' : {'read_only':True}
        }
