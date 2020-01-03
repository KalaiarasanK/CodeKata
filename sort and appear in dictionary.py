#Ria is a 5 year old girl. Her mother wants to teach her how to sort words in the same order that they appear in a dictionary. She decides to write a program to sort a given set of strings based on their alphabetical order. Help Ria’s mother to complete the program.


s = int(input())
a = [input() for i in range(s)]
a.sort()
print(*a,sep="\n",end="")
