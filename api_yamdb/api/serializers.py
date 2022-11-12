from django.shortcuts import get_object_or_404
from django.db.models import Avg
from rest_framework import serializers

from reviews.models import Review, Comments, Title, Genres, Categories
from users.models import User


class CategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = Categories
        fields = ('name', 'slug',)


class GenreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genres
        fields = ('name', 'slug',)


class TitlesSerializer(serializers.ModelSerializer):
    """Serializer модели Titles"""
    genre = GenreSerializer(many=True, read_only=True)
    category = CategorySerializer(read_only=True)
    rating = serializers.SerializerMethodField()

    def get_rating(self, obj):
        rating = obj.reviews.aggregate(Avg('score')).get('score__avg')
        if not rating:

            return rating

        return round(rating, 1)

    class Meta:
        fields = ('id', 'name', 'year', 'rating',
                  'description', 'genre', 'category',)
        model = Title


class TitlesCreateSerializer(serializers.ModelSerializer):
    """CreateSerializer модели Titles"""
    category = serializers.SlugRelatedField(
        slug_field='slug',
        queryset=Categories.objects.all()
    )
    genre = serializers.SlugRelatedField(
        slug_field='slug',
        queryset=Genres.objects.all(),
        many=True
    )

    class Meta:
        fields = ('id', 'name', 'year', 'description', 'genre', 'category',)
        model = Title


class ReviewSerializers(serializers.ModelSerializer):
    author = serializers.SlugRelatedField(slug_field='username',
                                          read_only=True, )

    def validate(self, data):
        request = self.context["request"]
        title_id = self.context["view"].kwargs.get("titles_id")
        title = get_object_or_404(Title, pk=title_id)
        if request.method == "POST":
            if Review.objects.filter(
                    title=title, author=request.user
            ).exists():

                raise serializers.ValidationError(
                    "Отзыв автора уже оставлен на данное произведение.")
        return data

    class Meta:
        fields = ('id', 'text', 'author', 'score', 'pub_date',)
        model = Review


class CommentSerializers(serializers.ModelSerializer):
    author = serializers.StringRelatedField(read_only=True)
    pub_date = serializers.DateTimeField(read_only=True)

    class Meta:
        fields = ('id', 'text', 'author', 'pub_date',)
        model = Comments


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = (
            'username',
            'email',
            'first_name',
            'last_name',
            'bio',
            'role'
        )
        lookup_field = ('username',)


class MeSerializer(serializers.ModelSerializer):
    role = serializers.CharField(read_only=True)

    class Meta:
        model = User
        fields = (
            'username',
            'email',
            'first_name',
            'last_name',
            'bio',
            'role'
        )


class SignUpSerializer(serializers.Serializer):
    email = serializers.EmailField(max_length=254, required=True)
    username = serializers.CharField(max_length=150, required=True)

    def validate(self, data):
        if data['username'] == 'me':

            raise serializers.ValidationError('Нельзя использовать логин me')

        return data

    class Meta:
        fields = ('username', 'email')


class TokenSerializer(serializers.Serializer):
    """Сериализатор для авторизации пользователя."""
    username = serializers.CharField(max_length=255)
    confirmation_code = serializers.CharField(max_length=128)
