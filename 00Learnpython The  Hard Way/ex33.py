def while_loop(N,numbers):
	i = 0
	while i < N:
		print("At the top i is %d" % i)
		numbers.append(i)

		i = add_num(i)
		print("Numbers now:",numbers)
		print("At the bottom i is %d" % i)

	print("Print the numbers:")
	for num in numbers:
		print(num)

def add_num(i):
	return i + 1

N = 10
list_n = []
while_loop(N,list_n)