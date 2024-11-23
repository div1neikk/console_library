import json
from typing import List, Optional


class Book:
    """Инициализируем родительский класс для наследования"""
    def __init__(self, id: int, title: str, author: str, year: int, status: str = "в наличии"):
        self.id = id
        self.title = title
        self.author = author
        self.year = year
        self.status = status

    def to_dict(self) -> dict:
        return {
            "id": self.id,
            "title": self.title,
            "author": self.author,
            "year": self.year,
            "status": self.status
        }

    @classmethod
    def from_dict(cls, data: dict):
        return cls(data["id"], data["title"], data["author"], data["year"], data["status"])


class Library:
    """Инициализируем родительский класс библиотеки с методами"""
    def __init__(self, storage_file: str = "storage.json"):
        self.storage_file = storage_file
        self.books: List[Book] = self.load_books()

    def load_books(self) -> List[Book]:
        try:
            with open(self.storage_file, "r", encoding="utf-8") as file:
                data = json.load(file)
                return [Book.from_dict(book) for book in data]
        except FileNotFoundError:
            return []
        except json.JSONDecodeError:
            print("Ошибка чтения файла.")
            return []

    def save_books(self) -> None:
        with open(self.storage_file, "w", encoding="utf-8") as file:
            json.dump([book.to_dict() for book in self.books], file, ensure_ascii=False, indent=4)

    def add_book(self, title: str, author: str, year: int) -> None:
        new_id = max((book.id for book in self.books), default=0) + 1
        new_book = Book(new_id, title, author, year)
        self.books.append(new_book)
        print(f"Книга '{title}' добавлена!")

    def remove_book(self, book_id: int) -> None:
        book = self.find_book_by_id(book_id)
        if book:
            self.books.remove(book)
            print(f"Книга с ID {book_id} удалена.")
        else:
            print("Книга с таким ID не найдена.")

    def find_book_by_id(self, book_id: int) -> Optional[Book]:
        return next((book for book in self.books if book.id == book_id), None)

    def search_books(self, **kwargs) -> List[Book]:
        key, value = next(iter(kwargs.items()))
        return [book for book in self.books if str(getattr(book, key)).lower() == str(value).lower()]

    def change_status(self, book_id: int, status: str) -> None:
        book = self.find_book_by_id(book_id)
        if book:
            if status in ["в наличии", "выдана"]:
                book.status = status
                print(f"Статус книги с ID {book_id} изменен на '{status}'.")
            else:
                print("Некорректный статус. Используйте 'в наличии' или 'выдана'.")
        else:
            print("Книга с таким ID не найдена.")

    def display_books(self) -> None:
        if not self.books:
            print("Библиотека пуста.")
        else:
            for book in self.books:
                print(f"{book.id}. {book.title} ({book.author}, {book.year}) - {book.status}")
