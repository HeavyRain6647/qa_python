from main import BooksCollector

# класс TestBooksCollector объединяет набор тестов, которыми мы покрываем наше приложение BooksCollector
# обязательно указывать префикс Test
class TestBooksCollector:

    # пример теста:
    # обязательно указывать префикс test_
    # дальше идет название метода, который тестируем add_new_book_
    # затем, что тестируем add_two_books - добавление двух книг
    def test_add_new_book_add_two_books(self):
        # создаем экземпляр (объект) класса BooksCollector
        collector = BooksCollector()

        # добавляем две книги
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_new_book('Что делать, если ваш кот хочет вас убить')

        # проверяем, что добавилось именно две
        # словарь books_rating, который нам возвращает метод get_books_rating, имеет длину 2
        assert len(collector.get_books_rating()) == 2

    # напиши свои тесты ниже
    # чтобы тесты были независимыми в каждом из них создавай отдельный экземпляр класса BooksCollector()
    # Тестирование добавления одной книги
    def test_add_new_book_single_book(self):
        collector = BooksCollector()
        collector.add_new_book('Война и мир')
        assert 'Война и мир' in collector.books_genre

    # Тестирование установки жанра книги
    @pytest.mark.parametrize("book_name, genre", 
                            [("Гарри Поттер", "Фантастика"),
                             ("Оно", "Ужасы"),
                             ("Шерлок Холмс", "Детективы")])
    def test_set_book_genre(self, book_name, genre):
        collector = BooksCollector()
        collector.add_new_book(book_name)
        collector.set_book_genre(book_name, genre)
        assert collector.get_book_genre(book_name) == genre

    # Тестирование получения жанра книги
    @pytest.mark.parametrize("book_name, genre", 
                            [("Алиса в стране чудес", "Мультфильмы"),
                             ("Франкенштейн", "Ужасы"),
                             ("Код да Винчи", "Детективы")])
    def test_get_book_genre(self, book_name, genre):
        collector = BooksCollector()
        collector.add_new_book(book_name)
        collector.set_book_genre(book_name, genre)
        assert collector.get_book_genre(book_name) == genre

    # Тестирование фильтрации по жанру
    @pytest.mark.parametrize("genre, books", 
                            [("Ужасы", ["Оно", "Франкенштейн"]),
                             ("Детективы", ["Шерлок Холмс", "Код да Винчи"])])
    def test_get_books_with_specific_genre(self, genre, books):
        collector = BooksCollector()
        for book in books:
            collector.add_new_book(book)
            collector.set_book_genre(book, genre)
        result = collector.get_books_with_specific_genre(genre)
        assert set(result) == set(books)

    # Тестирование получения всех книг
    def test_get_books_genre(self):
        collector = BooksCollector()
        books = ["Война и мир", "Гарри Поттер", "Маленький принц"]
        for book in books:
            collector.add_new_book(book)
        books_dict = collector.get_books_genre()
        for book in books:
            assert book in books_dict

    # Тестирование детских книг
    @pytest.mark.parametrize("book_name, genre", 
                            [("Колобок", "Мультфильмы"),
                             ("Теремок", "Мультфильмы"),
                             ("Дюймовочка", "Мультфильмы")])
    def test_get_books_for_children(self, book_name, genre):
        collector = BooksCollector()
        collector.add_new_book(book_name)
        collector.set_book_genre(book_name, genre)
        children_books = collector.get_books_for_children()
        assert book_name in children_books

    # Тестирование избранного
    @pytest.mark.parametrize("book_name", 
                            ["Властелин колец",
                             "Гарри Поттер",
                             "Маленький принц"])
    def test_favorites_functionality(self, book_name):
        collector = BooksCollector()
        collector.add_new_book(book_name)
        collector.add_book_in_favorites(book_name)
        assert book_name in collector.favorites

        
# Тестирование удаления из избранного
@pytest.mark.parametrize("book_name", 
["Властелин колец", "Гарри Поттер", "Маленький принц"])
def test_delete_from_favorites(self, book_name):
    collector = BooksCollector()
    collector.add_new_book(book_name)
    collector.add_book_in_favorites(book_name)
    
    # Проверяем добавление в избранное
    assert book_name in collector.favorites
    
    # Удаляем и проверяем удаление
    collector.delete_book_from_favorites(book_name)
    assert book_name not in collector.favorites