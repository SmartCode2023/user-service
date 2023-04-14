# File which contains the SHORT serializers for each model
from rest_framework import serializers

# User and Person Model
from apps.users.models.user import User, Person

# --------------------------------------------SHORT SERIALIZERS--------------------------------------------

# User and Person serializers
class UserSerializerShort(serializers.ModelSerializer):
    '''
    User serializer SHORT
        - id
        - first_name
        - last_name
        - email
        - phone_number
        - identification_type
        - identification_number
        - role
    '''
    
    class Meta:
        model = User
        fields = ('id', 'first_name', 'last_name', 'email', 'phone_number', 'identification_type', 'identification_number', 'role')
        
class PersonSerializerShort(serializers.ModelSerializer):
    '''
    Person serializer SHORT
        - id
        - first_name
        - last_name
        - email
        - phone_number
        - identification_type
        - identification_number
    '''
    
    class Meta:
        model = Person
        fields = ('id', 'first_name', 'last_name', 'email', 'phone_number', 'identification_type', 'identification_number')
    