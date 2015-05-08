from itertools import permutations

'''
Problem 4 from the blog post
'''

def find_largest(l):
	max = 0
	for p in permutations(l):
		value = int(reduce(lambda x,y: str(x)  +  str(y),p))
		if value > max:
			max = value
	return max

digits = range(1,10)

'''
Problem 5 from the post
'''

#Function to flatten a list
def concat(x):
	return reduce(lambda p,q: str(p) + ' ' +  str(q),x)

#Takes an expression with spaces before and after the + and - only
def parse(expr):
	expr = expr.split()
	element = None

	while len(expr) > 1:
		head = expr.pop()
		if head == "+":
			return int(parse(concat(expr))) + int(element)
		elif head == "-":
			return int(parse(concat(expr))) - int(element)
		else: 
			element = head

	return int(expr.pop())

#Retursn a list of all possible expressions from [1..9], and +,-,''
def possible(input):
	results = list()
	if len(input) > 1:
		for op in [' + ',' - ','']:
			for p in possible(input[1:]):
				results.append(str(input[0]) + op + p)  
	else: 
		return str(input[0])

	return results

#Find all expressions which equal 100
def solve():
	valid = list()
	for i in possible(digits):
		if parse(i) == 100:
			valid.append(i)

	return valid





