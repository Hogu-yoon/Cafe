from rest_framework import permissions


class CustomReadOnly(permissions.BasePermission):
    '''
    글 조회 : 누구나 , 생성 : 로그인 유저, 편집 : 해당 판매자
    '''

    def has_permission(self, request, view):
        if request.method == 'GET':
            return True
        return request.user.is_authenticated

    '''
        객체에 접근시 필요한 권환 확인
    '''

    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        return obj.seller == request.user
