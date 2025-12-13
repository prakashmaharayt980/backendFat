from rest_framework import serializers
from django.contrib.auth.password_validation import validate_password
from .models import User



class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(
        write_only=True,
        required=True,
        min_length=8,

        style={"input_type": "password"}
    )

    class Meta:
        model = User
        fields = ('email', 'password', 'name', 'phone', 'address')

    def validate_email(self, value):
        """
        Check if email already exists.
        """
        if User.objects.filter(email=value).exists():
            raise serializers.ValidationError("A user with this email already exists.")
        return value

    def create(self, validated_data):
        password = validated_data.pop("password")

        user = User(
            email=validated_data["email"],
            name=validated_data.get("name"),
            phone=validated_data.get("phone"),
            address=validated_data.get("address"),
        )
        user.set_password(password)   # HASHES PASSWORD
        user.save()

        return user

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'email', 'name', 'phone', 'address', 'date_joined', 'is_staff')
        read_only_fields = ('id', 'email', 'date_joined', 'is_staff')


class ChangePasswordSerializer(serializers.Serializer):
    old_password = serializers.CharField(required=True, write_only=True)
    new_password = serializers.CharField(required=True, write_only=True, min_length=8, validators=[validate_password])
    new_password_confirm = serializers.CharField(required=True, write_only=True)

    def validate(self, data):
        if data['new_password'] != data['new_password_confirm']:
            raise serializers.ValidationError({"new_password": "New passwords do not match."})
        return data

    def validate_old_password(self, value):
        user = self.context['request'].user
        if not user.check_password(value):
            raise serializers.ValidationError("Old password is incorrect.")
        return value