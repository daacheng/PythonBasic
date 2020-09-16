## Excel文件处理
#### 读取excel,处理不同类型的单元格
```python
import xlrd

filepath = r''
book = xlrd.open_workbook(filepath)
sheet = book.sheet_by_index(0)
rows = sheet.nrows
cols = sheet.ncols
for i in range(0, rows):
    for j in range(0, cols):
        cell_type = sheet.cell(i, j).ctype
        # 0:empty 1:string 2:number 3:date 4:boolean 5:error
        cell_value = sheet.cell(i, j).value
        if cell_type == 0:
            cell_value = ''
        elif cell_type == 2:
            cell_value = str(int(cell_value))
        elif cell_type == 3:
            cell_date = xlrd.xldate_as_tuple(cell_value, book.datemode)
            print(cell_date)
```

#### 读取Excel文件
```python
import xlrd  
# 读excel文件  
book = xlrd.open_workbook('test_copy.xlsx')  
book.sheets()  
sheet = book.sheet_by_index(0)  
# 查看行数和列数  
sheet.nrows  
sheet.ncols  
# 获取指定单元格内容  
# text:'RID'  
sheet.cell(0,0)     
# 获取指定行  
sheet.row(0)      #[text:'RID', text:'income1', text:'income2']  
sheet.row(1)      #[number:1.0, number:100.0, number:200.0]  
# 获取指定行单元格里的值  
sheet.row_values(1)     #[1.0, 100.0, 200.0]  
# 第一个参数是行索引，第二个参数是从第几个单元格开始取值  
sheet.row_values(1,1)   #[100.0, 200.0]  
# 添加单元格,参数依次为行索引，列索引，单元格格式，单元格内容，None  
sheet.put_cell(1,3,xlrd.XL_CELL_TEXT,'new cell',None)  
# [1.0, 100.0, 200.0, 'new cell']  
sheet.row_values(1)
```

#### 生成Excel文件
```python
import xlwt  
# 创建excel工作表  
workbook = xlwt.Workbook(encoding='utf-8')  
worksheet = workbook.add_sheet('sheet1')  
# 设置表头 (第一个参数为行数，第二个参数为单元格位置，第三个参数为单元格值)  
worksheet.write(0, 0, label='MAC')  
worksheet.write(0, 1, label='IMSI')  
worksheet.write(0, 2, label='IMEI')  
row_num = 1  

res = ['a', 'b', 'c']  
for i in res:  
    # 设置值 (第一个参数为行数，第二个参数为单元格位置，第三个参数为单元格值)  
    worksheet.write(row_num, 0, '1111')  
    worksheet.write(row_num, 1, i)  
    worksheet.write(row_num, 2, i)  
    row_num += 1  
workbook.save('OK.xls')  
```

#### 生成Excel文件
```python
from openpyxl import Workbook  
wb = Workbook()    # 创建文件对象  
ws = wb.active     # 获取第一个sheet  
ws.append(['MAC','IMSI','IMEI'])  
ws.append([11111,'2','3'])  
wb.save("OK.xlsx") 
```
