#Each new term in the Fibonacci sequence is generated by adding the 
#previous two terms. 
#By starting with 1 and 2, the first 10 terms will be 1,2,3,5,8
#By considering the terms in the Fibonacci sequence whose values 
#do not exceed four million, find the sum of the even-valued terms

fib=[1,2]  #make an empty list
sum = 0  #initialize
#fib.append(1)     #add two number to the first two list
#fib.append(2)
#fib[2] = fib[0]+fib[1]    cant use indexing like this need to append

n=1
while fib[n] <4000000:
	fib.append(fib[n]+fib[n-1])
	#print(fib[n]) prints fiboncci series
	if fib[n] %2 ==0:
		sum = sum + fib[n]
		#print(sum)
	n+=1
print(sum)
	