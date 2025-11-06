# -*- coding: utf-8 -*-
from main import BooksCollector
import pytest


@pytest.fixture
def books():
    return BooksCollector()


class TestBooksCollector:

    @pytest.mark.parametrize('name', ['The Witcher', 'The Witcher 2', 'Sherlock'])
    def test_add_new_book(self, books, name):
        check = len(books.books_genre)
        books.add_new_book(name)
        assert check + 1 == len(books.books_genre)

    @pytest.mark.parametrize('name,genre', [['The Witcher', 'Фантастика'], ['The Witcher 2', 'Фантастика'],
                                            ['Sherlock', 'Детективы']])
    def test_set_book_genre(self, books, name, genre):
        if name not in books.books_genre:
            books.add_new_book(name)
        books.set_book_genre(name, genre)
        print(books.books_genre)
        assert books.books_genre[name] == genre

    def test_get_book_genre(self, books):
        books.add_new_book('The Witcher')
        books.set_book_genre('The Witcher', 'Фантастика')
        assert books.get_book_genre('The Witcher') == 'Фантастика'

    def test_get_books_with_specific_genre(self, books):
        books.books_genre = {'Sherlock': 'Детективы', 'The Witcher 2': 'Фантастика', 'The Witcher': 'Фантастика'}
        result = len(books.get_books_with_specific_genre('Фантастика'))
        assert result == 2

    def test_get_books_genre(self, books):
        books.books_genre = {'Sherlock': 'Детективы', 'The Witcher 2': 'Фантастика', 'The Witcher': 'Фантастика'}
        assert books.get_books_genre() == books.books_genre

    def test_get_books_for_children(self, books):
        books.books_genre = {'Sherlock': 'Детективы', 'The Witcher 2': 'Фантастика', 'The Witcher': 'Фантастика'}
        children_books = {'The Witcher', 'The Witcher 2'}
        result = books.get_books_for_children()
        assert set(result) == children_books

    def test_add_book_in_favorites(self, books):
        books.books_genre = {'Sherlock': 'Детективы', 'The Witcher 2': 'Фантастика', 'The Witcher': 'Фантастика'}
        books.add_book_in_favorites('The Witcher 2')
        assert 'The Witcher 2' in books.favorites

    def test_delete_book_from_favorites(self, books):
        books.books_genre = {'Sherlock': 'Детективы', 'The Witcher 2': 'Фантастика', 'The Witcher': 'Фантастика'}
        books.add_book_in_favorites('The Witcher 2')
        books.delete_book_from_favorites('The Witcher 2')
        assert 'The Witcher 2' not in books.favorites

    def test_get_list_of_favorites_books(self, books):
        books.books_genre = {'Sherlock': 'Детективы', 'The Witcher 2': 'Фантастика', 'The Witcher': 'Фантастика'}
        books.add_book_in_favorites('The Witcher 2')
        books.add_book_in_favorites('The Witcher')
        assert books.get_list_of_favorites_books() == ['The Witcher 2', 'The Witcher']
