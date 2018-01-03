#encoding='utf-8'
#count 2-3+4-5+6....+100-101
l=[i for i in range(2,102)]
sum=0
result=''
for i in l:
	if i%2==0:
		sum+=i
		result+=('+'+str(i))
	else:
		sum-=i
		result+=str(-i)
print(sum)
print(result,'=',sum)