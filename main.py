from logic_lib import Library


def main():
    library = Library()

    while True:
        print("\nМеню:")
        print("1. Добавить книгу")
        print("2. Удалить книгу")
        print("3. Искать книгу")
        print("4. Показать все книги")
        print("5. Изменить статус книги")
        print("6. Выйти")

        choice = input("Введите номер действия: ")
        if choice == "1":
            title = input("Введите название книги: ")
            author = input("Введите автора: ")
            year = int(input("Введите год издания: "))
            library.add_book(title, author, year)
        elif choice == "2":
            book_id = int(input("Введите ID книги: "))
            library.remove_book(book_id)
        elif choice == "3":
            key = input("Искать по (title/author/year): ")
            value = input("Введите значение для поиска: ")
            results = library.search_books(**{key: value})
            for book in results:
                print(f"{book.id}. {book.title} ({book.author}, {book.year}) - {book.status}")
        elif choice == "4":
            library.display_books()
        elif choice == "5":
            book_id = int(input("Введите ID книги: "))
            status = input("Введите новый статус ('в наличии' или 'выдана'): ")
            library.change_status(book_id, status)
        elif choice == "6":
            library.save_books()
            print("До свидания!")
            break
        else:
            print("Некорректный ввод. Попробуйте снова.")


if __name__ == "__main__":
    main()
