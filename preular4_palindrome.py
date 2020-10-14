#A palindromic number reads
# the same both ways. The largest palindrome made from the
#product of two 2-digit numbers is 9009 = 91 × 99.
#Find the largest palindrome made from the product of two 3-digit numbers.

#First start with a = 999 and b = 999, decrese b while a constant
#999*999 999*998 999*997...999*1 then when b = 1 change b to 999 and 
#decrese a by 1 like 998 * 999......998*990....998*1 then change
#let p be the product than change p to string because you can check value
#of string at different positions like p2[2] = some number
#store the number by append and the value of a and b
#use index to know the index of largest product and use it to find a and b

a = 999
b=999
lar=[]
av=[]
bv=[]
while a > 1:
	if b==1:
		b=999
	while b>1:
		p = a*b
		p1=str(p)
		
		if len(p1)==6:
			if p1[0]==p1[5] and p1[1]==p1[4] and p1[2]==p1[3]:
				lar.append(p)
				av.append(a)
				bv.append(b)
				

		if len(p1)==5:
			if p1[0]==p1[4] and p1[1]==p1[3]:
				lar.append(p)
				av.append(a)
				bv.append(b)
				
		b-=1
	a-=1

print(max(lar))
ind = lar.index(max(lar))
print(av[ind])
print(bv[ind])

