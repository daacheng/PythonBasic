一、爬取百度招聘信息，存入MongoDB。 baidu_spider.py

二、通过公司名称，爬取手机号（这一步最终是将合法的手机号存入phonenum表）
    2.1、从“职位描述”字段中提取手机号，存入phonenum表中，主键是“公司名称”。 utils.py   find_phone_from_desc()
    2.2、从数据库读取"公司名称"字段，去重，生成company_name.csv文件。  utils.py  get_company_name_to_csv()
    2.3、读取company_name.csv文件，通过公司名称，爬取公司电话，存入MongoDB的company_phone表中。(这个表临时存公司-电话信息)  shunqi.py
    2.4、读取 company_phone表中的数据，对手机号进行校验，合格的存入 phonenum 表中。  utils.py  clear_phone_of_company_phone()

三、读取phonenum表中的 公司-电话 到字典中，然后读取数据库中招聘数据，根据‘公司名称’去获取公司电话，将数据添加到  job_data_list列表中。 utils.py  get_data_of_job()

四、清洗job_data_list列表中的数据。 utils.py  clear_job_data(job_data_list)

五、生成excel文件。