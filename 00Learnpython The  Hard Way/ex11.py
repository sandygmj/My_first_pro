print ("How old are you?",)
age = input()
print ("How tall are you?",)
height = input()
print("How much do you weight?",)
weight = input()

print("So, you are %r old, %r tall, and %r heavy." % (age,height,weight))
#在SublimeText中编译执行时，需要input和raw_input的时候，需要安装SublimetextREPL,同时在编译的时候可以设置快捷键，
#此处的快捷键设置为f5