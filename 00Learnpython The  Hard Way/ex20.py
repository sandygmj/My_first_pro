from sys import argv

script,input_file = argv

def print_all(f):
	print(f.read())

def rewind(f):
	f.seek(0)#seek是将指针的位置放回文件首位

def print_a_line(line_count,f):
	print(line_count,f.readline())#打印第line_count的内容，第一个参数是行号，第二个参数是读取这一行的内容，即readline这个方法是用于读取

current_file = open(input_file)

print("First let's print the whole file:\n")
print_all(current_file)

print("Now let's rewind, kind of like a tape.")
rewind(current_file)

print("Let's print three lines.")

current_line = 1
print_a_line(current_line,current_file)
current_line = current_line + 1
print_a_line(current_line,current_file)
current_line = current_line + 1
print_a_line(current_line,current_file)
current_file.close()#打开的文件要记得关闭，养成编程的良好习惯。