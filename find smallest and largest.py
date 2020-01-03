#Given a number N followed by N numbers.Find the smallest number and largest number and print both the indices(1 based indexing).


a=int(input())
b=list(map(int,input().split()))
print(min(b),max(b))
