from rest_framework import serializers
from snippets.models import Snippet
from django.contrib.auth.models import User

class SnippetSerializer(serializers.ModelSerializer):
    owner_id = serializers.PrimaryKeyRelatedField(
        source='owner',
        queryset = User.objects.all(),
    )
    owner = serializers.ReadOnlyField(source="owner.username")
    class Meta:
        model = Snippet
        fields = ('id', 'title', 'code', 'owner', 'owner_id')

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'email')
