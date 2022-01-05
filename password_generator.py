from string import *
from random import sample
import sys

def random_password(k):
	"""Generates a random password using digits, ascii letters, and ponctuations

	Args:
		k (int): Number of characters in the password
	Returns:
		string password
	"""
	digit = digits
	lower_case = ascii_lowercase
	upper_case = ascii_uppercase
	ponct = punctuation
	password = digits + lower_case + upper_case + ponct 

	return(''.join(sample(list(password), int(k))))


if __name__ == '__main__':
	print(globals()[sys.argv[1]](sys.argv[2]))
