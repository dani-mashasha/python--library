from datetime import date

class Reader:
    unique_id = 1
    def __init__(self, name):
        self.id = Reader.unique_id
        self.name = name
        self.books = []
        Reader.unique_id+=1

    def read_book(self, title):
        today = str(date.today())
        read_book = {"title": title, "date": today}
        self.books.append(read_book)