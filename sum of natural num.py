#Write a program to print the sum of the first K natural numbers.


def findSum(n) : 
	sum = 0
	x = 1
	while x <=n : 
		sum = sum + x 
		x = x + 1
	return sum

print(findSum(3))
