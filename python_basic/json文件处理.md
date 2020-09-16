## json文件处理
#### json.dumps(): 把Python对象转换成字符串
#### json.loads(): 把字符串转换成Python对象

```python
import json   
#dumps() 把python对象转换成json字符串  
p_dict={'c':'aaa','b':'ss','a':'dd'}  

# 字典转换成json格式字符串  
# '{"a": "dd", "b": "ss", "c": "aaa"}'  
json.dumps(p_dict,sort_keys=True)  

# json格式字符串转换成字典  
obj = json.loads('{"a": "dd", "b": "ss", "c": "aaa"}')  
# dict  
print(type(obj))  

obj2 = json.loads('["aaa","bbb",222]')  
# list  
print(type(obj2))   

# 把Python对象写入到.json文件中  
l=['a','b','{"c":1,"d":2}']  
with open('dump.json','w') as f:  
    json.dump(l,f)  
# 读取.json文件  
with open('dump.json','r') as f:  
    # ['a', 'b', '{"c":1,"d":2}']  
    print(json.load(f))  
```
