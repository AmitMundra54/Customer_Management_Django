from rest_framework import serializers
from core.models import User

class UserReadSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('first_name','middle_name','last_name','gender','date_of_birth','organisation','department','personal_email',
                  'current_address','permanent_address','role','designation','phone_number',)
