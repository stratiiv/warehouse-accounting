from rest_framework import permissions


class IsProductOwnerOrReadOnly(permissions.BasePermission):
    """
    Custom permission to allow only the product owner to edit or delete,
    others have read-only access.
    """
    def has_object_permission(self, request, view, obj) -> bool:
        """"
        Check if the request user has permission to perform the given action
        on the product object.
        """
        if request.method in permissions.SAFE_METHODS:
            return True
        return obj.user == request.user


def has_edit_permission(request, product) -> bool:
    """
    Check if the request user has edit permission on the specified product.
    """
    if request.user.is_authenticated and product.user == request.user:
        return True
    return False
