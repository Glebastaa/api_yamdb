from django.contrib import admin

from reviews.models import (
    Review, Comments, Categories, Genres, GenreTitle, Title
)


@admin.register(Title)
class TitleAdmin(admin.ModelAdmin):
    """Настройка параметров отображения произведений в админке"""

    list_display = (
        'pk',
        'name',
        'category',
    )
    list_editable = ('name', 'category')
    search_fields = ('name',)
    empty_value_display = '-пусто-'


@admin.register(Categories)
class CategoryAdmin(admin.ModelAdmin):
    """Настройка параметров отображения категорий в админке"""

    list_display = (
        'pk',
        'name',
        'slug',
    )
    list_editable = ('name', 'slug')
    search_fields = ('name',)
    empty_value_display = '-пусто-'


@admin.register(Genres)
class GenreAdmin(admin.ModelAdmin):
    """Настройка параметров отображения жанров в админке"""

    list_display = (
        'pk',
        'name',
        'slug',
    )
    search_fields = ('name',)
    empty_value_display = '-пусто-'


@admin.register(GenreTitle)
class GenreTitleAdmin(admin.ModelAdmin):
    """Настройка параметров отображения
    свяски произведение-жанр в админке"""

    list_display = (
        'pk',
        'title',
        'genre',
    )
    search_fields = ('name',)
    empty_value_display = '-пусто-'


@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    """Настройка параметров отображения отзывов в админке"""

    list_display = (
        'pk',
        'author',
        'title',
        'text',
        'score',
        'pub_date'
    )
    list_editable = ('text', 'score')
    empty_value_display = '-пусто-'


@admin.register(Comments)
class CommentAdmin(admin.ModelAdmin):
    """Настройка параметров отображения отзывов в админке"""

    list_display = (
        'pk',
        'author',
        'review',
        'text',
        'pub_date'
    )
    list_editable = ('text',)
    empty_value_display = '-пусто-'
