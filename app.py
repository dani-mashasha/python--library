import pymongo
from pymongo import MongoClient
from modules.Library import Library
from modules.Shelf import Shelf
from modules.Book import Book
from initial_data import initial_data
import math
import requests
import json 
from dotenv import load_dotenv
import os

load_dotenv()

DB_USER=os.getenv("DB_USER")
DB_PASS=os.getenv("DB_PASS")
DB_NAME=os.getenv("DB_NAME")
DB_COLLECTION=os.getenv("DB_COLLECTION")
DB_HOST=os.getenv("DB_HOST")

cluster = MongoClient(f"mongodb+srv://{DB_USER}:{DB_PASS}@{DB_HOST}/?retryWrites=true&w=majority")
db = cluster[DB_NAME]
collection = db[DB_COLLECTION]


def check_database():
    res = collection.find_one({})
    if not res:
        collection.insert_many(initial_data)
        print("Books added to the DataBase...\n")
    else:
        print("DataBase is full...\n")

def initial_shelves(books, shelves):
    index = 0
    for book in books:
        book_to_add = Book(book["author"], book["title"], book["num_of_pages"])
        shelves[math.floor(index)].addBook(book_to_add)
        index += 0.5

def verify_user():
    username = input("Enter Username: ")
    email = input("Enter Email: ")

    url = "https://jsonplaceholder.typicode.com/users"
    params={"username": username, "email": email}
    user = requests.get(url,params ).json()
    if user:
        menu()
    else:
        verify_user()
   

def menu():
    str = "-For adding a book - Press 1.\n-For deleting a book - Press 2.\n-For changing books locations - Press 3.\n-For registering a new reader - Press 4.\n-For removing a reader - Press 5.\n-For searching books by author – Press 6.\n-For reading a book by a reader – Press 7.\n-For ordering all books – Press 8.\n-For saving all data – Press 9.\n-For loading data – Press 10.\n-For exit – Press 11.\n"
    action = int(input(str))

    if action == 1:
        author = input("Enter the autor name: ")
        title = input("Enter the book title: ")
        num_of_pages = input("Enter the number of pages in the book: ")
        library.add_new_book(Book(author, title, num_of_pages))

    elif action == 2:
        title = input("Enter the title of the book you wish to remove: ")
        library.delete_book(title)

    elif action == 3:
        first_title = input("Enter the first book title: ")
        second_title = input("Enter the second book title: ")
        library.change_locations(first_title, second_title)

    elif action == 4:
        reader_name = input("Enter new reader name: ")
        library.register_reader(reader_name)

    elif action == 5:
        reader_name = input("Enter the name of the reader you wish to remove: ")
        library.remove_reader(reader_name)

    elif action == 6:
        author_name = input("Enter the author name: ")
        author_books = library.search_by_author(author_name)
        if author_books != []:
            print(author_books)
        else:
            print("No books found by this author...")
        input("Press any key to go back to the menu")
    
    elif action == 7:
        reader_name = input("Enter the reader name: ")
        title = input("Enter the book title: ")
        library.reader_read_book( reader_name, title)

    elif action == 8:
        library.order_books()

    elif action == 9:
        file_name = input("Enter file name: ")
        library_json = library.toJson()

        with open(file_name, "w") as outfile:
            json.dump(library_json, outfile, indent = 4)


    elif action == 10:
        file_name = input("Enter file name: ")
        file = open(file_name)
        data = json.load(file)
        print(json.dumps(data, indent=4))
        input("\nPress any key to go back to the menu")

    elif action == 11:
        exit()
    
    menu()


## initialize bd
check_database()

##initialize shelves
books_data = collection.find({})
shelves = [Shelf(),Shelf(),Shelf()]
initial_shelves(books_data, shelves)

##Create library
library = Library(shelves)

##Starts the program
verify_user()

