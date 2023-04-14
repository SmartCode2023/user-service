from apps.shared.shared_api.shared_views.GenericModelViewSets import GenericModelViewSet

from apps.users.api.serializers import UserViewSerializer, UserCreateSerializer

from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import status

class UserViewSet(GenericModelViewSet):
    serializer_class = UserViewSerializer
    serializer_create_class = UserCreateSerializer
    serializer_update_class = UserCreateSerializer
    
    @action(detail=False, methods=['post'])
    def login(self, request):
        """Login a user.

        Args:
            request (POST): HTTP request information
                - email
                - password
        """
        email = request.data.get('email')
        password = request.data.get('password')
        model = self.get_serializer().Meta.model
        
        if not email or not password:
            return Response({'error': 'Email and password are required'}, status=status.HTTP_400_BAD_REQUEST)

        user = model.objects.filter(email=email).first()
        if not user:
            return Response({'error': 'Invalid credentials'}, status=status.HTTP_400_BAD_REQUEST)
        
        if not user.check_password(password):
            return Response({'error': 'Invalid credentials'}, status=status.HTTP_400_BAD_REQUEST)
        
        if not user.is_active:
            return Response({'error': 'User is not active'}, status=status.HTTP_400_BAD_REQUEST)
        
        serializer = self.get_serializer(user)
        if serializer.data:
            return Response(serializer.data, status=status.HTTP_200_OK)
        