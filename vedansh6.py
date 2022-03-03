"""Write a program to calculate salary of an employee with following condition
1)if basic salary is <10000
then HRA=20% and DA=80%
2)if basic salary is >10000 and <=20000
then HRA=25% and DA=85%
1)if basic salary is >20000
then HRA=30% and DA=95%"""
s=int(input("Enter the basic salary of employee")
if (s<10000):
	hra=(20*s)/100
	da=(80*s)/100
	print("The salaray of emplyoee is %f"%(s+hra+da))
elif(s>10000 and s<=20000):
	hra=(25*s)/100
	da=(85*s)/100
	print("The salaray of emplyoee is %f"%(s+hra+da))
elif(s>20000):
	hra=(30*s)/100
	da=(95*s)/100
	print("The salaray of emplyoee is %f"%(s+hra+da))

