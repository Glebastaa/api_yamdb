import uuid

from django.db import models
from django.contrib.auth import get_user_model
from django.core.validators import MaxValueValidator, MinValueValidator


User = get_user_model()


class Categories(models.Model):
    """Инициализация модели Category."""
    name = models.CharField(max_length=200)
    slug = models.SlugField(unique=True, default=uuid.uuid1)

    def __str__(self):
        return self.name


class Genres(models.Model):
    """Инициализация модели Genre."""
    name = models.CharField(max_length=200)
    slug = models.SlugField(unique=True, default=uuid.uuid1)

    def __str__(self):
        return self.name


class Title(models.Model):
    """Инициализация модели Title."""
    name = models.CharField(max_length=200)
    category = models.ForeignKey(
        Categories, on_delete=models.SET_NULL,
        related_name="titles", blank=True, null=True
    )
    year = models.IntegerField(
        default=2022, validators=[
            MinValueValidator(1900), MaxValueValidator(2100)
        ]
    )
    description = models.TextField(blank=True)
    genre = models.ManyToManyField(
        Genres, through='GenreTitle'
    )

    def __str__(self):
        return self.name


class GenreTitle(models.Model):
    """Инициализация модели GenreTitle."""
    title = models.ForeignKey(Title, on_delete=models.CASCADE)
    genre = models.ForeignKey(Genres, on_delete=models.CASCADE)

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=['title', 'genre'],
                name='unique_genretitle'
            ),
        ]

    def __str__(self):
        return f'{self.genre} {self.title}'


class Review(models.Model):
    """Инициализация модели Review."""
    author = models.ForeignKey(
        User, on_delete=models.CASCADE,
        related_name='reviews', blank=False
    )
    title = models.ForeignKey(
        Title, on_delete=models.CASCADE, related_name='reviews')
    text = models.TextField()
    score = models.IntegerField(default=5, validators=[MinValueValidator(1),
                                MaxValueValidator(10)])
    pub_date = models.DateTimeField(
        'Дата добавления', auto_now_add=True, db_index=True)

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=['author', 'title'],
                name='unique_review'
            ),
        ]

    def __str__(self):
        return self.text


class Comments(models.Model):
    """Инициализация модели Comment."""
    author = models.ForeignKey(
        User, on_delete=models.CASCADE,
        related_name='comments', blank=False
    )
    review = models.ForeignKey(
        Review, on_delete=models.CASCADE, related_name='comments')
    text = models.TextField()
    pub_date = models.DateTimeField(
        'Дата добавления', auto_now_add=True, db_index=True)

    def __str__(self):
        return self.text
