# Program to print Fibonacci Series upto 'n'

n=int(input("Enter the value of n - "))
a=0
b=1
sum=a+b
print("Fibonacci series -")
print(a)
print(b)
print(sum)
for i in range(n-3):
	a=b
	b=sum
	sum=a+b
	print(sum)