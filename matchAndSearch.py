'''
re模块中match(pattern,string[,flags]),检查string的开头是否与pattern匹配。
re模块中research(pattern,string[,flags]),在string搜索pattern的第一个匹配值。
'''
import re
print(re.match('a','abc').span()) #(0,1)
print(re.match('b','abc')) #None
print(re.search('a','li is a dog name').span())#(6,7)
print(re.search('name','li is a dog name').span())#(12,16)