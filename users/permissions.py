from rest_framework import permissions


class CustomReadOnly(permissions.BasePermission):
    '''
    객체에 접근시 필요한 권환 확인
    '''
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        return obj.user == request.user
