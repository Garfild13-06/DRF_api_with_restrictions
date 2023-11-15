from rest_framework.permissions import BasePermission


class IsOwnerOrReadOnly(BasePermission):
    # def has_permission(self, request, view):
    def has_object_permission(self, request, view, obj):
        # print(request.method)
        if request.method == 'GET':
            return True
        # разрешаем админу все действия
        if request.user.username == 'admin':
            return True
        return request.user.id == obj.creator.id
