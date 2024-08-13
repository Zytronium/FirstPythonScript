from ctypes import c_char
from time import sleep


def iterate_to(n):
	i = 0
	while i <= n:
		print(i)
		i += 1
	print('done.')

def iterate_to_letter(n):
	i = 'A' if 'A' <= n <= 'Z' else 'a'
	while i <= n:
		print(i)
		i = chr(ord(i)+1)
	print('done.')