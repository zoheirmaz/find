from django.contrib.auth.models import User
from rest_framework import serializers

from first.models import WebPage, topics


class UserSerializer(serializers.Serializer):
    # class Meta:
    #     model = User
    #     fields = ('url', 'username', 'email', 'groups')
    id = serializers.IntegerField(read_only=True)
    url = serializers.URLField(required=False, allow_blank=True, max_length=100)
    username = serializers.CharField(max_length=256, allow_blank=True, required=False)
    email = serializers.EmailField(max_length=256, required=False)

    def create(self, validated_data):
        """
        Create and return a new `Snippet` instance, given the validated data.
        """
        return User.objects.create(**validated_data)

    def update(self, instance, validated_data):
        """
        Update and return an existing `Snippet` instance, given the validated data.
        """
        instance.id = validated_data.get('id', instance.id)
        instance.url = validated_data.get('url', instance.url)
        instance.username = validated_data.get('username', instance.username)
        instance.email = validated_data.get('email', instance.email)
        # instance.style = validated_data.get('style', instance.style)
        instance.save()
        return instance


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    # class Meta:
    #     model = Group
    #     fields = ('url', 'name')

    id = serializers.IntegerField(read_only=True)
    url = serializers.URLField(required=False, allow_blank=True, max_length=100)
    username = serializers.CharField(max_length=256, allow_blank=True, required=False)
    email = serializers.EmailField(max_length=256, required=False)

    def create(self, validated_data):
        """
        Create and return a new `Snippet` instance, given the validated data.
        """
        return User.objects.create(**validated_data)

    def update(self, instance, validated_data):
        """
        Update and return an existing `Snippet` instance, given the validated data.
        """
        instance.id = validated_data.get('id', instance.id)
        instance.url = validated_data.get('url', instance.url)
        instance.username = validated_data.get('username', instance.username)
        instance.email = validated_data.get('email', instance.email)
        # instance.style = validated_data.get('style', instance.style)
        instance.save()
        return instance


# class WebPageSerializer(serializers.HyperlinkedModelSerializer):
#     # class Meta:
#     #     model = WebPage
#     #     fields = ('name', 'topic')
#
#     id = serializers.IntegerField(read_only=True)
#     url = serializers.URLField(required=False, allow_blank=True, max_length=100)
#     username = serializers.CharField(max_length=256, allow_blank=True, required=False)
#     email = serializers.EmailField(max_length=256, required=False)
#
#     def create(self, validated_data):
#         """
#         Create and return a new `Snippet` instance, given the validated data.
#         """
#         return User.objects.create(**validated_data)
#
#     def update(self, instance, validated_data):
#         """
#         Update and return an existing `Snippet` instance, given the validated data.
#         """
#         instance.id = validated_data.get('id', instance.id)
#         instance.url = validated_data.get('url', instance.url)
#         instance.username = validated_data.get('username', instance.username)
#         instance.email = validated_data.get('email', instance.email)
#         # instance.style = validated_data.get('style', instance.style)
#         instance.save()
#         return instance


class WebPageSerializer(serializers.ModelSerializer):
    class Meta:
        model = WebPage
        fields = '__all__'


class TopicSerializer(serializers.ModelSerializer):
    class Meta:
        model = topics
        fields = '__all__'
