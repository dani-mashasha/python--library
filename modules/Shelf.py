class Shelf:
    def __init__(self):
        self.books = []
        self.is_shelf_full= False
    

    def addBook(self, book):
        if self.is_shelf_full:
            print("No more room on the shelf")
            return
        else:
            self.books.append(book)
            if len(self.books) == 5:
                self.is_shelf_full = True 

    def replace_books(self, first_location, second_location):
        length = len(self.books)
        if  first_location < 1 or first_location > length :
            print(f"Cant find a book in location {first_location}")
            return 0
        elif second_location < 1 or second_location > length:
            print(f"Cant find a book in location {second_location}")
            return 0
        else:
            first_book = self.books[first_location-1] 
            second_book = self.books[second_location-1]
            self.books[first_location-1] = second_book
            self.books[second_location-1] = first_book


    def order_books(self):
        length = len(self.books)
        for i in range(length):
            for j in range(length - i - 1):
                if self.books[j].num_of_pages > self.books[j + 1].num_of_pages:
                    self.books[j], self.books[j + 1] = self.books[j + 1], self.books[j]


