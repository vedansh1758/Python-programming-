#write a program to enter the side of triangles and find triangle can be formed or not.
x=int(input("enter 1st side"))
y=int(input("enter 2nd side"))
z=int(input("enter 3rd side"))
if((x+y)>z and (x+z)>y and (y+z)>x):
	print("Valid triangle")
else:
	print("Invalid triangle")

