from rest_framework import serializers
from rest_framework.relations import SlugRelatedField
from rest_framework.validators import UniqueTogetherValidator

from posts.models import Comment, Post, Group, Follow


class GroupSerializer(serializers.ModelSerializer):

    class Meta:
        model = Group
        fields = '__all__'


class FollowSerializer(serializers.ModelSerializer):
    user = SlugRelatedField(slug_field='username', read_only=True,
                            default=serializers.CurrentUserDefault())
    following = SlugRelatedField(slug_field='username', read_only=True,
                                 default=serializers.CurrentUserDefault())

    class Meta:
        model = Follow
        exclude = ('id',)
        validators = [
            UniqueTogetherValidator(
                queryset=Follow.objects.all(),
                fields=('user', 'following')
            )
        ]

#         Проверьте, что при POST запросе на `/api/v1/follow/` с неправильными данными возвращается статус 400
# E       assert 404 == 400
# E         +404
# E         -400


class PostSerializer(serializers.ModelSerializer):
    author = SlugRelatedField(slug_field='username', read_only=True)

    class Meta:
        fields = '__all__'
        model = Post


class CommentSerializer(serializers.ModelSerializer):
    author = serializers.SlugRelatedField(
        read_only=True, slug_field='username'
    )

    class Meta:
        fields = '__all__'
        model = Comment
