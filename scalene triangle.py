#Given 3 numbers A,B,C print 'yes' if they can form the sides of a scalene triangle else print 'no'.

x = int(input())
y = int(input())
z = int(input())

if x==y or y==z or z==x:
	print("No")
else:
	print("yes")
