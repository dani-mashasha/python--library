from modules.Book import Book
from modules.Shelf import Shelf
from modules.Reader import Reader
from modules.Library import Library


b1 = Book("dani", "life", 10)
b2 = Book("gil", "giz", 5)
b3 = Book("shy", "frind", 13)
b4 = Book("david", "foo", 7)
b5 = Book("king", "myking", 11)
b6 = Book("dama", "queen", 12)
b7 = Book("king", "myhsha", 20)
b8 = Book("hghg", "myhgh", 14)
b9 = Book("king", "myvbvb", 5)
b10 = Book("mkmkm", "mykmkmk", 24)
b11 = Book("jcjc", "myjcjc", 15)
b12 = Book("opop", "myopop", 8)

sh1 = Shelf()
sh2 = Shelf()
sh3 = Shelf()

l1 = Library([sh1, sh2, sh3])

l1.add_new_book(b1)
l1.add_new_book(b2)
l1.add_new_book(b3)
l1.add_new_book(b4)
l1.add_new_book(b5)
l1.add_new_book(b6)
l1.add_new_book(b7)
l1.add_new_book(b8)
l1.add_new_book(b9)
l1.add_new_book(b10)
l1.add_new_book(b11)
l1.add_new_book(b12)


l1.register_reader("dani")
l1.register_reader("dddaaa")
l1.register_reader("nniii")


for r in l1.readers:
    print(r.name, r.id)