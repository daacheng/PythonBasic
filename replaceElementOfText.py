import re
#re.compile()编译正则表达式模式，返回一个对象的模式。（可以把那些常用的正则表达式编译成正则表达式对象，这样可以提高一点效率。）
'''
sub(replacement, string[,count=0])
（replacement是被替换成的文本，string是需要被替换的文本，count是一个可选参数，指最大被替换的数量）

subn()方法执行的效果跟sub()一样，不过它会返回一个二维数组，包括替换后的新的字符串和总共替换的数量
'''
p=re.compile('blue|yellow')
print(p.sub('red','blue and yellow is my favorite color.'))#red and red is my favorite color.
print(p.subn('red','blue and yellow is my favorite color.'))#('red and red is my favorite color.', 2)