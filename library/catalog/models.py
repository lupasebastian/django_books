from django.db.models import Model, CharField, IntegerField, ForeignKey, DO_NOTHING, DateField, TextField


# Create your models here.


class Author(Model):
    name = CharField(max_length=128, verbose_name='Imię i nazwisko', unique=True)

    def __str__(self):
        return self.name


class Book(Model):
    title = CharField(max_length=128, verbose_name='Tytuł')
    genre = CharField(max_length=128, verbose_name='Gatunek')
    rating = IntegerField(verbose_name='Ocena')
    author = ForeignKey(Author, on_delete=DO_NOTHING, verbose_name='Autor')
    issue_date = DateField(verbose_name='Data wydania')
    description = TextField(verbose_name='Opis')

    def __str__(self):
        return self.title
