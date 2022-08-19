from modules.Reader import Reader
import json

class Library:
    def __init__(self, shelves):
        self.shelves = shelves
        self.readers = []

    def toJson(self):
        return json.loads(json.dumps(self, default=lambda o : o.__dict__,  indent=4))

    def is_there_place_for_new_book(self):
        for shelf in self.shelves:
            if not shelf.is_shelf_full:
                return True
        return False
    
    def add_new_book(self, book_obj):
        for shelf in self.shelves:
            if not shelf.is_shelf_full:
                shelf.addBook(book_obj)

                return 1
        return 0 

    def delete_book(self, title):
        for shelf in self.shelves:
            for i in range(len(shelf.books)):
                if shelf.books[i].title == title:
                    shelf.books.pop(i)
                    return 1
        return 0 

    def change_locations(self, first_title, second_title):
        first_book = {}
        second_book = {}
        first_book_location = []
        second_book_location = []
        for i in range(len(self.shelves)):
            for j in range(len(self.shelves[i].books)):
                if self.shelves[i].books[j].title == first_title:
                    first_book = self.shelves[i].books[j]
                    first_book_location = [i,j]
                elif self.shelves[i].books[j].title == second_title:
                    second_book = self.shelves[i].books[j]
                    second_book_location = [i,j]

        if first_book and second_book:
            self.shelves[first_book_location[0]].books[first_book_location[1]] = second_book
            self.shelves[second_book_location[0]].books[second_book_location[1]] = first_book
        else:
            print("Somting went wrong!")

    def change_locations_in_same_shelf(self, shelf_num, first_location, second_location):
        self.shelves[shelf_num-1].replace_books(first_location, second_location)

    def order_books(self):
        for shelf in self.shelves:
            shelf.order_books()

    def register_reader(self, reader_name):
        new_reader = Reader(reader_name)
        self.readers.append(new_reader)

    def remove_reader(self, reader_name):
         for i in range(len(self.readers)):
                if self.readers[i].name == reader_name:
                    self.readers.pop(i)
                    break
    
    def reader_read_book(self, reader_name, title):
        for reader in self.readers:
            if reader.name == reader_name:
                reader.read_book(title)

    def search_by_author(self, author_name):
        books_by_author = []
        for shelf in self.shelves:
            for book in shelf.books:
                if book.author == author_name:
                    books_by_author.append(book.title)
        return books_by_author
