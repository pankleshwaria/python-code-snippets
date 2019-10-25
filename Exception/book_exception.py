class BookException(Exception):

	def __init__(self, error_type, error):
		self.error_type = error_type
		self.error = error
		
	def print_error(self):
		print( f"Error Type: {self.error_type} Error: {self.error}" )