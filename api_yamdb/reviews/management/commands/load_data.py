from csv import DictReader
from django.core.management import BaseCommand

from reviews.models import (
    Categories, Genres, Title,
    Review, Comments, GenreTitle
)
from users.models import User


class Command(BaseCommand):

    def handle(self, *args, **options):
        if Categories.objects.exists():
            print('Данные уже импортированы')
            return
        print("Загрузка category.csv")
        category = [
            Categories(
                id=row['id'],
                name=row['name'],
                slug=row['slug'],
            )
            for row in DictReader(
                open(
                    './static/data/category.csv',
                    encoding="utf-8"
                )
            )
        ]
        Categories.objects.bulk_create(category)

        genre = [
            Genres(
                id=row['id'],
                name=row['name'],
                slug=row['slug'],
            )
            for row in DictReader(
                open(
                    './static/data/genre.csv',
                    encoding="utf-8"
                )
            )
        ]
        Genres.objects.bulk_create(genre)

        titles = [
            Title(
                id=row['id'],
                name=row['name'],
                year=row['year'],
                category=Categories.objects.get(pk=row['category']),
            )
            for row in DictReader(
                open(
                    './static/data/titles.csv',
                    encoding="utf-8"
                )
            )
        ]
        Title.objects.bulk_create(titles)

        users = [
            User(
                id=row['id'],
                username=row['username'],
                email=row['email'],
                role=row['role'],
                bio=row['bio'],
                first_name=row['first_name'],
                last_name=row['last_name']
            )
            for row in DictReader(
                open(
                    './static/data/users.csv',
                    encoding="utf-8",
                )
            )
        ]
        User.objects.bulk_create(users)

        review = [
            Review(
                id=row['id'],
                text=row['text'],
                author=User.objects.get(pk=row['author']),
                score=row['score'],
                pub_date=row['pub_date'],
                title=Title.objects.get(pk=row['title_id']),
            )
            for row in DictReader(
                open(
                    './static/data/review.csv',
                    encoding="utf-8",
                )
            )
        ]
        Review.objects.bulk_create(review)

        comments = [
            Comments(
                id=row['id'],
                review=Review.objects.get(pk=row['review_id']),
                text=row['text'],
                author=User.objects.get(pk=row['author']),
                pub_date=row['pub_date'],
            )
            for row in DictReader(
                open(
                    './static/data/comments.csv',
                    encoding="utf-8",
                )
            )
        ]
        Comments.objects.bulk_create(comments)

        genre_title = [
            GenreTitle(
                id=row['id'],
                title=Title.objects.get(pk=row['title_id']),
                genre=Genres.objects.get(pk=row['genre_id']),
            )
            for row in DictReader(
                open(
                    './static/data/genre_title.csv',
                    encoding="utf-8",
                )
            )
        ]
        GenreTitle.objects.bulk_create(genre_title)
        print('Импорт успешно завершён')
