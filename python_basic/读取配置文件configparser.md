## 读取配置文件(configparser)
#### 配置文件格式:
```python
[mysql]  
host = 172.16.2.207  
port = 3306  
db = WWW  
user = EEE  
passwd = 123445  

[csv]  
print_num = 100000
```
#### 读取配置内容：

```python
import configparser  

# 配置文件由节(sections)、键(key)、值(value)组成  
config = configparser.ConfigParser()  
config.read("all_export_conf", encoding='utf-8')  

# 获取配置文件所有的节sections   ['mysql', 'csv']  
config.sections()  

# 获取某个节中的所有键   ['host', 'port', 'db', 'user', 'passwd']  
config.options('mysql')  

# 获取某个节中的某个键对应的value   '172.16.2.207'  
config.get('mysql','host')  
config.get('mysql','port')  

# 添加一个配置文件节点  
config.add_section('test')  

# 给节点添加键值对  
config.set('test','name','daacheng')  
```
