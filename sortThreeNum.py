a=input("please input a:")
b=input("please input b:")
c=input("please input c:")
l=[]
l.append(int(a))
l.append(int(b))
l.append(int(c))
print(sorted(l))
#for i in sorted(l,reverse=True):
#	print(i)
for i in sorted(l):
	print(i)