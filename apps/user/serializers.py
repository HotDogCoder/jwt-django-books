from rest_framework import serializers

from apps.user.models import UserAccount

class UserAccountSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserAccount
        fields = [
            'username',
            'email',
            'first_name',
            'last_name',
            'is_active',
            'is_staff',
            'verified',
            'requested_verified',
            'picture',
            'banner',
            'location',
            'url',
            'birthday',
            'profile_info',
        ]
