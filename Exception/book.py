from book_exception import BookException

class Book:

	book_list = []

	def __init__(self, id, name, author):
		self.id = id
		self.name = name
		self.author = author
		
	@staticmethod
	def get_all_books():
		return Book.book_list
	
	@staticmethod	
	def add_book(book_obj):
		if book_obj.validate_book(book_obj) is True:
			Book.book_list.append(book_obj)
			
	def validate_book(self, obj_book):
		if not obj_book.id:
			raise BookException("Error", "Id is required")
		if not obj_book.name:
			raise BookException("Error", "Name is required")
		if not obj_book.author:
			raise BookException("Error", "Author is required")
		return True
		
book1 = Book(1, "The monk who sold his Ferrari", "Robin Sharma")
book2 = Book(2, "Fault in our stars", "‎John Green")
book3 = Book(3, "The Godfather", "Mario Puzo")

Book.add_book(book1)
Book.add_book(book2)
Book.add_book(book3)

books = Book.get_all_books()
for book in books:
	print(f"id: {book.id} name: {book.name} author: {book.author}")

# raises exception
# book4 = Book(4, "XYZ", "")
# Book.add_book(book4)