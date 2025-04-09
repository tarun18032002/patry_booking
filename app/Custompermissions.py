from rest_framework import permissions


class IsOwnerorAdmin(permissions.BasePermission):
    """     
    Custom permission to only allow owners of an object or admins to view/edit it.
    
    """

    def has_object_permission(self, request, view, obj):
        # Admin can do anything
        if request.user.role== 'admin':
            return True
        
        # User/Organizers can only access their own data
        return obj.id == request.user.id
    
class IsOrganizer(permissions.BasePermission):
    """
    Custom permission to only allow organizers to acces the view.
    """

    def has_permission(self, request, view):
        return bool(request.user and request.user.is_authenticated and request.user.role == 'organizer')
    

class IsAdminUser(permissions.BasePermission):
    """
    Custom permission to only allow admins user to acess the view.
    
    """

    def has_permission(self, request, view):
        return request.user.role == 'admin'