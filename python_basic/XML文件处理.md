## 创建XML文件
```python
import xml.dom.minidom as Dom   
# 创建XML文档  
doc = Dom.Document()  
# 创建根节点  
root = doc.createElement('html')  
# 创建h1节点  
h1 = doc.createElement('h1')  
h1.setAttribute('name','aaaa')  
h1.setAttribute('value','hhhhh')  

h1.appendChild(doc.createTextNode('hello world'))  

doc.appendChild(root)  
# 把h1节点作为root的子节点进行添加  
root.appendChild(h1)  

f = open(r"C:\Users\daacheng\Desktop\test2.xml", "w",encoding='utf-8')    
doc.writexml(f, addindent='\t', newl='\n', encoding="utf-8")   
f.close()
```
## XML文件解析

```python
from xml.etree.ElementTree import parse  
from xml.etree.ElementTree import parse  
#解析简单的xml文档  
data = open('data.xml')  
et = parse(data)  
# xml.etree.ElementTree.ElementTree  
type(et)  
root = et.getroot()  
root.tag  
root.attrib  
# findall()只能寻找当前节点子节点内的标签  
for child in root.findall('RecordTime'):  
    for child_two in child:  
        print(child_two.tag)  
# iter()可以递归查找当前节点下所有子孙节点标签  
list(root.iter('Year'))
```
## XML字符串解析

```python
import xml.etree.ElementTree as ET
root = ET.fromstring(body)
devicelist = root.find('DeviceList')
items = devicelist.findall('Item')
for item in items:
    camera_sip_id = item.findtext('DeviceID')  # 设备sip_id
    camera_name = item.findtext('Name')  # 设备名称
    camera_address = item.findtext('Address')  # 设备IP
    camera_org = item.findtext('Manufacturer')  # 设备厂商
    camera_model = item.findtext('Model')  # 设备型号
```
