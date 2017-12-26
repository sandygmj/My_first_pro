from sys import argv

script,filename = argv

txt = open(filename)

print("Here's your file %r" % filename)
print(txt.read())#打印读取文件中的内容.read为读取文件
txt.close()
#以上方法为通过调用从agrv传递参数的方法
#下面的方法为手动输入文件名传递参数，打开文件读取文件内容的方法。
print("Type the filename again:")
file_again = input(">")
#此时输入的文件名也可以时ex15.py 本身，即自己输出自己的内容。有意思。ß
txt_again = open(file_again)

print (txt_again.read())