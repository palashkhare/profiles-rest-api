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
