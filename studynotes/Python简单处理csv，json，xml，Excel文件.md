# Python简单处理csv，json，xml，Excel文件
## Python读写csv文件

        import csv
        #Python读写csv文件
        with open('test.csv','r') as r_file:
            reader = csv.reader(r_file)
            with open('test_copy.csv','w',newline='') as w_file:
                writer = csv.writer(w_file)
                for row in reader:
                    writer.writerow(row)
        print('end')

## Python处理json文件

        import json 
        #dumps() 把python对象转换成json字符串
        p_dict={'c':'aaa','b':'ss','a':'dd'}
        json.dumps(p_dict)             #'{"c": "aaa", "b": "ss", "a": "dd"}'
        type(json.dumps(p_dict))       #str
        json.dumps(p_dict,sort_keys=True)     #'{"a": "dd", "b": "ss", "c": "aaa"}'

        #loads()  把json字符串转换成Python对象
        obj = json.loads('{"a": "dd", "b": "ss", "c": "aaa"}')
        type(obj)                    #dict

        obj2 = json.loads('["aaa","bbb",222]')
        type(obj2)                   #list

        #dump()   把Python对象写入到.json文件中
        l=['a','b','{"c":1,"d":2}']
        with open('dump.json','w') as f:
            json.dump(l,f)
        #load()  读取.json文件
        with open('dump.json','r') as f:
            print(json.load(f))               #['a', 'b', '{"c":1,"d":2}']

## Python处理xml文档
### 解析简单的xml文档

        from xml.etree.ElementTree import parse
        #解析简单的xml文档
        data = open('data.xml')
        et = parse(data)
        type(et)             #xml.etree.ElementTree.ElementTree
        root = et.getroot()
        root.tag
        root.attrib
        #findall()只能寻找当前节点子节点内的标签
        for child in root.findall('RecordTime'):
            for child_two in child:
                print(child_two.tag)
        #iter()可以递归查找当前节点下所有子孙节点标签
        list(root.iter('Year'))
### 构建xml文档

        from xml.etree.ElementTree import Element,ElementTree,tostring
        #构建xml文档
        #创建元素
        e = Element('data')
        e.tag                #'data'
        #设置标签属性
        e.set('name','aaa')
        e.attrib             #{'name': 'aaa'}
        e.text='123'
        tostring(e)          #<data name="aaa">123</data>

### 把csv文件转换成xml格式

        from xml.etree.ElementTree import Element,ElementTree,tostring
        import csv
        #把csv格式转换成xml格式
        with open('test.csv','r',newline='') as f:
            reader = csv.reader(f)
            heads = next(reader)
            root = Element('data')
            for row in reader:
                eRow = Element('row')
                root.append(eRow)
                for tag,text in zip(heads,row):
                    e=Element(tag)
                    e.text=text
                    eRow.append(e)
                #print(tostring(eRow))
            et=ElementTree(root)
            et.write('demo.xml')
## Python处理Excel文件
### 读取Excel

        import xlrd
        #读excel文件
        book = xlrd.open_workbook('test_copy.xlsx')
        book.sheets()
        sheet = book.sheet_by_index(0)
        #查看行数和列数
        sheet.nrows
        sheet.ncols
        #获取指定单元格内容
        sheet.cell(0,0)   #text:'RID'
        #获取指定行
        sheet.row(0)      #[text:'RID', text:'income1', text:'income2']
        sheet.row(1)      #[number:1.0, number:100.0, number:200.0]
        #获取指定行单元格里的值
        sheet.row_values(1)     #[1.0, 100.0, 200.0]
        #第一个参数是行索引，第二个参数是从第几个单元格开始取值
        sheet.row_values(1,1)   #[100.0, 200.0]
        #添加单元格,参数依次为行索引，列索引，单元格格式，单元格内容，None
        sheet.put_cell(1,3,xlrd.XL_CELL_TEXT,'new cell',None)
        sheet.row_values(1)         #[1.0, 100.0, 200.0, 'new cell']

### 写Excel(.xls)

        import xlwt
        # 创建excel工作表
        workbook = xlwt.Workbook(encoding='utf-8')
        worksheet = workbook.add_sheet('sheet1')
        # 设置表头 (第一个参数为行数，第二个参数为单元格位置，第三个参数为单元格值)
        worksheet.write(0, 0, label='MAC')
        worksheet.write(0, 1, label='IMSI')
        worksheet.write(0, 2, label='IMEI')
        worksheet.write(0, 3, label='微信')
        worksheet.write(0, 4, label='QQ')
        worksheet.write(0, 5, label='淘宝')
        worksheet.write(0, 6, label='京东')
        worksheet.write(0, 7, label='滴滴')
        worksheet.write(0, 8, label='美团')
        worksheet.write(0, 9, label='新浪微博')
        worksheet.write(0, 10, label='腾讯微博')
        worksheet.write(0, 11, label='旺信')
        worksheet.write(0, 12, label='米聊')
        worksheet.write(0, 13, label='YY语音')

        row_num = 1

        res = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',]
        for i in res:
            # 设置值 (第一个参数为行数，第二个参数为单元格位置，第三个参数为单元格值)
            worksheet.write(row_num, 0, '1111')
            worksheet.write(row_num, 1, i)
            worksheet.write(row_num, 2, i)
            worksheet.write(row_num, 3, i)
            worksheet.write(row_num, 4, i)
            worksheet.write(row_num, 5, i)
            worksheet.write(row_num, 6, i)
            worksheet.write(row_num, 7, i)
            worksheet.write(row_num, 8, i)
            worksheet.write(row_num, 9, i)
            worksheet.write(row_num, 10, i)
            worksheet.write(row_num, 11, i)
            worksheet.write(row_num, 12, i)
            worksheet.write(row_num, 13, i)
            row_num += 1


        workbook.save('OK.xls')
### 写Excel(.xlsx)

        from openpyxl import Workbook
        wb = Workbook()    # 创建文件对象
        ws = wb.active     # 获取第一个sheet
        ws.append(['MAC','IMSI','IMEI','微信','QQ','淘宝','京东','滴滴','美团','新浪微博','腾讯微博','旺信','米聊','YY语音'])
        ws.append([11111,'2','3'])
        wb.save("OK.xlsx")
