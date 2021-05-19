from rest_framework import permissions


class UpdateOwnProfile(permissions.BasePermission):
    """ Allow users to edit own profiles
        Django provides BasePermission class to allow users to add custom
        permissions
    """

    def had_object_permission(self, request, view, obj):
        """Check if user is trying to edit its own profile"""
        print(str(permissions.SAFE_METHODS))
        if request.method in permissions.SAFE_METHODS:
            print("SAFE_METHODS", request.method)
            return True
        print("unSAFE_METHODS", request.method)
        return obj.id == request.user.id

class UpdateOwnStatus(permissions.BasePermission):
    """ Allow users to update their own status"""

    def has_object_permission(self, request, view, obj):
        """check if user is trying to update their own status """
        if request.method in permissions.SAFE_METHODS:
            return True

        # If user id in request is equal to User ID object which is being
        # modified, then return true
        print("Request User ID: ", request.user.id,
              " -- Object beig modified : ", obj)
              
        return request.user.id == obj.user_profile.id
