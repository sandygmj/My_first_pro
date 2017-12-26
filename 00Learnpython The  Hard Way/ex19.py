def cheese_and_crackers(cheese_count,boxes_of_crackers):
	print("You have %d cheeses!" % cheese_count)
	print("You have %d boxes of crackers!" % boxes_of_crackers)
	print("Man that's enough for a party!")
	print("Get a blanket.\n")
#函数的调用使用
#可以直接传数值作为参数
print("We can just give the function numbers directly:")
cheese_and_crackers(20,30)
#传变量作为参数
print("OR, we can use variables from our script:")
amount_of_cheese = 10
amount_of_crackers = 50

cheese_and_crackers(amount_of_cheese,amount_of_crackers)

#在传递参数时进行数学计算
print("We can even do math inside too:")
cheese_and_crackers(10+20,5+6)
#传递参数时，将变量和数字进行数学计算
print("And we can combine the two,variables and math:")
cheese_and_crackers(amount_of_cheese+100,amount_of_crackers+1000)