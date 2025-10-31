class BooksCollector:
    def __init__(self):
        self.books_genre = {}  # словарь: название → жанр
        self.favorites = []     # список избранных книг
        self.genre = ['Фантастика', 'Ужасы', 'Детективы', 'Мультфильмы', 'Комедии']
        self.genre_age_rating = ['Ужасы', 'Детективы']  # жанры с возрастным ограничением

    # Добавляем новую книгу (без жанра)
    def add_new_book(self, name):
        if not self.books_genre.get(name) and 0 < len(name) < 41:
            self.books_genre[name] = ''

    # Устанавливаем жанр книги (отдельная операция)
    def set_book_genre(self, name, genre):
        if name in self.books_genre and genre in self.genre:
            self.books_genre[name] = genre


    # Получаем жанр книги по названию
    def get_book_genre(self, name):
        return self.books_genre.get(name, None)  # None, если книги нет


    # Список книг заданного жанра
    def get_books_with_specific_genre(self, genre):
        books = []
        if genre in self.genre:
            for name, book_genre in self.books_genre.items():
                if book_genre == genre:
                    books.append(name)
        return books

    # Возвращаем полный словарь книг с жанрами
    def get_books_genre(self):
        return self.books_genre


    # Книги, подходящие для детей (не в genre_age_rating)
    def get_books_for_children(self):
        books = []
        for name, genre in self.books_genre.items():
            if genre not in self.genre_age_rating and genre in self.genre:
                books.append(name)
        return books

    # Добавляем книгу в Избранное
    def add_book_in_favorites(self, name):
        if name in self.books_genre and name not in self.favorites:
            self.favorites.append(name)

    # Удаляем книгу из Избранного
    def delete_book_from_favorites(self, name):
        if name in self.favorites:
            self.favorites.remove(name)


    # Получаем список Избранных книг
    def get_list_of_favorites_books(self):
        return self.favorites




