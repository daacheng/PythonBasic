import re
p=re.compile('\n|\W')
f=open('english.txt')
lines=f.readlines()
words=[]

for line in lines:
	#l=re.sub('\W',' ',line)
	l=line.replace(',','').replace('?','').strip()
	l=l.split(' ')
	words.extend(l)
	print(line)
print(words)
d=dict.fromkeys(words,0)
for x in words:
	d[x]+=1
z=zip(d.values(),d.keys())
s_z=sorted(z,reverse=True)
print(s_z)
f.close()
