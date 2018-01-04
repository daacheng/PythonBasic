import math
for i in range(1,10001):
	i1=i+100
	i2=i+268
	if (math.sqrt(i1)%1==0) and (math.sqrt(i2)%1==0):
		print(i)
		print(i1,':',math.sqrt(i1))
		print(i2,':',math.sqrt(i2))
		print('####################')
