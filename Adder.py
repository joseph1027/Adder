class Adder:
	def __init__(self, num1, num2):
		self.num1 = num1
		self.num2 = num2

	def add(self):
		sum = self.num1 + self.num2
		return sum

if __name__ == "__main__":
	A = Adder(1,3)
	result = A.add()
	print(result)
