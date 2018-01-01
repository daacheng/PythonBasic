a=[1,1,1,2,3,4,4]
#b=set(a)#{1,2,3,4}#方法一：使用set()方法
b=dict.fromkeys(a)#方法二：dict.fromkeys()方法转换成dict，然后取key
single=list(b.keys())#[1,2,3,4]
print(single)