#Find sum of multiples of 3 or 5
#Also you have to subtract from total the common multiple
sum3 = 0
sum5 = 0
com=0
n=1
b = 1
x=1

while (3*n) < 1000:
	sum3 = sum3 + 3*n
	n +=1
while (5*b) < 1000:
	sum5 = sum5 + 5*b
	b +=1
while (15*x) < 1000:  #common multiple of 3 and 5
	com = com + 15*x
	x +=1

sum = sum3 + sum5 - com
print(sum)
	

