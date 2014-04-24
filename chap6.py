# Enter your answrs for chapter 6 here
# Name: Tyler Wallace


# Ex. 6.6

def first(word):
	return word[0]

def last(word):
	return word[-1]

def middle(word):
	return word[1:-1]

#1. Nothing is returned if middle is called with a two letter word.
#print middle("ab")

#Nothing is returned if middle is called with a one letter word.
#print middle("a")

#Nothing is returned if middle is called with no word
#print middle("")

#2
def is_palindrome(word):
	if len(word) == 0:
		return True
	elif word[0] != word[-1]:
		return False
	else:
		return is_palindrome(word[1:-1])
# Ex 6.7


def is_power(a,b):
	if a%b > 0:
		return False
	elif a/b == 1 and a%b == 0:
		return True
	else:
		return is_power(a/b,b)


