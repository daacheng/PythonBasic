from pymongo import MongoClient
import csv
import xlwt
import random

client = MongoClient('localhost', 27017)
baidu = client.baidu
company_phone = baidu.company_phone
coll = baidu.work_1118



def save_company_phone_to_mongodb():
    """
        读取 'company_phone.csv'中的信息，存入数据库 company_phone表中
    """
    with open('company_phone.csv', 'r', encoding='utf-8') as f:
        reader = csv.reader(f, delimiter='\t')
        for row in reader:
            info ={
                'name': row[0],
                'phone': row[1]
            }
            company_phone.insert_one(info)


def get_company_phone_dict():
    """
        从数据库读取 公司-电话 信息，存入字典company_phone_dict
        key：公司名称， value: 公司电话
    """
    company_phone_dict = {}
    company_phone_list = company_phone.find()
    for info in company_phone_list:
        company_phone_dict[info['name']] = info['phone']
    return company_phone_dict


def get_data_of_company_phone():
    """
        从数据库读取  公司-电话 信息，存入‘company_phone.csv’文件
    """
    company_phone_list = company_phone.find()

    with open('company_phone.csv', 'w', encoding='utf-8', newline='') as f:
        writer = csv.writer(f, delimiter='\t')
        for info in company_phone_list:
            print(info['name'], info['phone'])
            writer.writerow([info['name'], info['phone']])


def clear_job_desc(job_desc):
    """
        对“招聘要求”进行清洗
    """
    job_desc = job_desc.replace('\n', '').replace('"', '').replace('\r', '').replace(' ', '')\
            .replace('请简单描述下项目的基本情况（可不填）', '').replace('进场前先核实对方身份证，杜绝先打路费现象。', '')\
            .replace('嘴子勿扰', '').replace('骗子勿扰', '').replace('回民勿扰', '').replace('回民误打扰', '')\
            .replace('由于生活习俗不同', '').replace('微信不回', '').replace('微信', '').replace('回民，勿扰', '').replace('微信同号', '')\
            .replace('回民不要', '').replace('不用回民', '').replace('回族人', '').replace('回族绕行', '').replace('回民绕道', '')\
            .replace('少数民族同胞勿扰', '').replace('少数民族', '').replace('因生活习惯不一样', '').replace('单身不要', '').replace('因生活习惯不同', '')\
            .replace('回族和彝族勿扰', '').replace('彝族勿扰', '').replace('回族勿扰', '').replace('回族朋友勿扰', '').replace('回民一律不要', '')\
            .replace('回民飞机头勿扰', '').replace('回民不招', '').replace('于由生活原因', '').replace('回民和', '').replace('因生活方式不同', '').replace('回民同胞暂不接收', '')\
            .replace('回民混子', '').replace('回族异族不要', '').replace('回族兄弟', '').replace('回族，', '').replace('回民，', '').replace('回民。', '').replace('回族忽扰', '')\
            .replace('回民不收', '').replace('骗子回民请勿扰', '').replace('回民忽扰', '').replace('回民优先', '').replace('回民不收', '')\
            .replace('因生活习俗不一样', '').replace('少数名族勿扰', '').replace('回族等勿扰', '').replace('回族因风俗习惯不同请勿扰', '') \
            .replace('回族及骗路费的勿扰', '').replace('回族骗路费的勿扰', '').replace('回族等勿扰谢谢', '').replace('回民兄弟勿扰', '').replace('回民及骗路费勿扰', '')\
            .replace('回民绕行', '').replace('回民朋友勿扰', '').replace('回民请饶行', '').replace('回族不要', '').replace('回民及骗路费的勿扰', '')\
            .replace('，回民', '').replace('回民无扰', '').replace('回民请绕道', '').replace('回民及骗路勿扰', '').replace('回民谢绝', '').replace('回民离我远点', '')\
            .replace('回民及提前打路费的勿扰', '').replace('&amp;', '').replace('nbsp;', '')
    return job_desc


def get_data_of_job():
    """
        从数据库中获取招聘数据，根据‘公司名称’去获取公司电话，将数据添加到  job_data_list列表中
    """
    job_data_list = []
    company_phone_dict = get_company_phone_dict()
    job_list = coll.find()

    for info in job_list:
        print(info)

        company = info['company']  # 公司名称

        phone = ''  # 公司电话
        if company in company_phone_dict.keys():
            phone = company_phone_dict[company]
        else:
            continue

        province = info['province']  # 省
        city = info['city']  # 市
        district = info['district']  # 区县
        title = info['title']  # 标题
        job_desc = info['job_desc']  # 职位描述

        job_desc = clear_job_desc(job_desc)

        detail_address = info['detail_address']  # 详细地址
        job_type = info['job_type']  # 工种
        release_time = info['release_time']  # 发布时间
        valid_time = info['valid_time']  # 有效时间
        salary = info['salary']  # 有效时间
        require = job_desc  # 职位要求
        status = info['status']  # 状态

        row = [company, province, city, district, title, job_desc, detail_address, job_type, release_time, valid_time, salary, require, phone, status]
        job_data_list.append(row)

    return job_data_list


def job_data_to_excel(job_data_list):

    # 创建excel工作表
    workbook = xlwt.Workbook(encoding='utf-8')
    worksheet = workbook.add_sheet('sheet1')

    for i in range(0, len(job_data_list)):
        worksheet.write(i, 0, label=job_data_list[i][0])
        worksheet.write(i, 1, label=job_data_list[i][1])
        worksheet.write(i, 2, label=job_data_list[i][2])
        worksheet.write(i, 3, label=job_data_list[i][3])
        worksheet.write(i, 4, label=job_data_list[i][4])
        worksheet.write(i, 5, label=job_data_list[i][5])
        worksheet.write(i, 6, label=job_data_list[i][6])
        worksheet.write(i, 7, label=job_data_list[i][7])
        worksheet.write(i, 8, label=job_data_list[i][8])
        worksheet.write(i, 9, label=job_data_list[i][9])
        worksheet.write(i, 10, label=job_data_list[i][10])
        worksheet.write(i, 11, label=job_data_list[i][11])
        worksheet.write(i, 12, label=job_data_list[i][12])
        worksheet.write(i, 13, label=job_data_list[i][13])
    workbook.save('OK2.xls')


def main():
    job_data_list = get_data_of_job()
    job_data_to_excel(job_data_list)
    # job_list = coll.find()
    # company_list = []
    # for info in job_list:
    #     if info['company'] not in company_list:
    #         company_list.append(info['company'])
    #
    # with open('company_1119.csv', 'w', encoding='utf-8', newline='') as f:
    #     writer = csv.writer(f, delimiter='\t')
    #     for item in company_list:
    #         writer.writerow([item])
    # save_company_phone_to_mongodb()

    # job_list = coll.find()
    #
    # for info in job_list:
    #     info['salary'] = random.randint(50, 70) * 100
    #     coll_1118.insert_one(info)


if __name__ == '__main__':
    main()
