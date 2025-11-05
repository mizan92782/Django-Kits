from rest_framework.permissions import BasePermission

class IsPremiumUser(BasePermission):
    """
    Allows access only to users in the 'PremiumUser' group.
    """

    def has_permission(self, request, view):
        user = request.user
        # Make sure the user is authenticated first
        if not user.is_authenticated:
            return False
        
        # Check if user is in the 'PremiumUser' group
        return user.groups.filter(name='PremiumUser').exists()
