from Adder import Adder

def test_add():
	a = 2
	b = 7
	t_case = Adder(a,b)
	assert t_case.add() == a+b, "AAAAA"