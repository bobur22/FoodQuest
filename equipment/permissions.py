from rest_framework import permissions

class IsAdminOrReadOnly(permissions.BasePermission):
    """
    Only admin can create/update/delete equipment.
    Others can read.
    """

    def has_permission(self, request, view):
        if request.method in permissions.SAFE_METHODS:
            return True
        return request.user.is_authenticated and request.user.role == 'admin'
