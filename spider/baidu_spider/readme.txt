1、爬取百度招聘信息，存入MongoDB。 baidu_spider.py

2、从数据库读取"公司名称"字段，生成company_name.csv文件。  utils.py  get_company_name_from_mongodb()

3、读取company_name.csv文件，通过公司名称，爬取公司电话，存入MongoDB的company_phone表中。

4、读取数据库中的 公司-电话 到字典中，然后读取数据库中招聘数据，根据‘公司名称’去获取公司电话，将数据添加到  job_data_list列表中。 utils.py  get_data_of_job()

5、清洗job_data_list列表中的数据。 utils.py  clear_job_data(job_data_list)

6、生成excel文件。