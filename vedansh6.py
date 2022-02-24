#Write a program to find whether the number is even or odd.
n=int(input("Enter the number"))
b=n&1
if(b==1):
	print("The number is even")
else:
	print("The number is odd")
