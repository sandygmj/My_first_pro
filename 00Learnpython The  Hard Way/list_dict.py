
a = [1,2,3,4,5]
print(a)
print(a[0])
print(a[-1])
a.insert(5,6)
print(a)
a.pop()
print(a)
a.pop(1)
print(a)
sandy = {'name':'郭敏杰','age':35,'weight':'75kg','tall':'175cm'}
print(sandy)
sandy['is_single'] = False#字典中添加新元素的方法
print(sandy)
from fun_demo import add  #调用同一目录下的fun_demo.py文件里面的add函数进行操作。
x = 1
y = 2
print(add(x,y))
from fun_demo import return_x_y,change_x_y
a,b = return_x_y(x,y)
print(a,b)
a,b = change_x_y(x,y)
print(a,b)