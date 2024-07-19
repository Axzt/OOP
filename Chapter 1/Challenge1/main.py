class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author


class Library:
    def __init__(self, name):
        self.name = name
        self.books = []

    def add_book(self, book):
        self.books.append(book)

    def remove_book(self, book):
       for all_book in self.books:
            if all_book.title == book.title:
                self.books.remove(all_book)
                break

    
    def search_books(self, search_string):
        search_result = []
        search = search_string.lower()
        for book in self.books:
            if search in book.title.lower() or search in book.author.lower():
                search_result.append(book)
        return search_result
