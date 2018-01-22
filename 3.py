#print("输入3个数据，以空格进行分割")
a,b,c=input( ).split(' ')
#b=input("输入第2个数字")
#c=input("输入第3个数字")
x=[]
x.append(int(a))
x.append(int(b))
x.append(int(c))


print(max(x))