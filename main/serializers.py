from .models import User
from .models import Translation
from rest_framework import serializers


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ['id', 'name', 'quota_limit', 'quota_spent']


class TranslationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Translation
        fields = '__all__'


class UserUpdateSerializer(serializers.ModelSerializer):
    name = serializers.CharField(required=False)
    quota_limit = serializers.IntegerField(required=False)
    quota_spent = serializers.IntegerField(required=False)

    class Meta:
        model = User
        fields = ['id', 'name', 'quota_limit', 'quota_spent']


class UpdateTranslationSerializer(serializers.ModelSerializer):
    from_user = serializers.PrimaryKeyRelatedField(queryset=User.objects.all())
    input_text = serializers.CharField(required=False)
    output_text = serializers.CharField(required=False)

    class Meta:
        model = Translation
        fields = ['id', 'from_user', 'input_text', 'output_text']
