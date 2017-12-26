from sys import argv
from os.path import exists

script,from_file,to_file = argv

print("Copying from %s to %s" % (from_file,to_file))

#We could do these two on one line too,how?
in_file = open(from_file)#打开文件
indata = in_file.read()#读取文件内容，并放在indata中

print("The input file is %d bytes long" % len(indata))

print("Does the output file exist? %r" % exists(to_file))#exists方法用于判断文件是否存在。
print("Ready, hit RETRUN to contine,CTR-C to abort.")
input()

out_file = open(to_file,'w')#若不存在to_file这个文件，直接创建一个。
out_file.write(indata)

print("Alright,all done.")

out_file.close()
in_file.close()