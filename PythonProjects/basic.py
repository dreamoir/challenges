# This is a basic program that wqill ask the user for a number(interger)
# and print sum


i=int(input("please enter an integer:  "))
sum=0
if int(i)-i == 0:
	num=str(i)
else:
	error('please enter an integer!')

for x in range (0,len(num)):
	digit=int(num[x])
	sum=sum+digit
	print("+",digit)

print("total sum of digits is : ",sum)
