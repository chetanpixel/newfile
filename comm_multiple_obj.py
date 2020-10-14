class Common_multiple():
	"""Eular problem"""
	def __init__(self,max_product):
		self.max_product = max_product
		

	def algorithm(self):
		sum3 = 0
		sum5 = 0
		com=0
		n=1
		b = 1
		x=1

		while (3*n) < self.max_product:
			sum3 = sum3 + 3*n
			n +=1
		while (5*b) < self.max_product:
			sum5 = sum5 + 5*b
			b +=1
		while (15*x) < self.max_product:
			com = com + 15*x
			x +=1
		sum = sum3 + sum5 - com
		return sum
	
	def print_sum(self):
		print(f"The sum of common multi is {self.algorithm()}")

number1 = Common_multiple(1000)
number1.print_sum()
number2 = Common_multiple(2000)
number2.print_sum()
number2.algorithm()
