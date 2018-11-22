from pymongo import MongoClient
import csv
import xlwt
import random
import re

shiqu_dict = {
    '北京': ['东城', '西城', '朝阳', '丰台', '石景山', '海淀', '门头沟', '房山', '通州', '顺义', '昌平', '大兴', '怀柔', '平谷', '密云', '延庆'],
    '天津': ['和平', '河北', '河东', '河西', '南开', '红桥', '东丽', '西青', '津南', '北辰', '武清', '宝坻', '滨海新', '宁河', '静海', '蓟州'],
    '太原': ['杏花岭', '迎泽', '小店', '尖草坪', '万柏林', '晋源'],
    '大同': ['平城', '云冈', '新荣', '云州', '阳高', '天镇', '广灵', '灵丘', '浑源', '左云'],
    '石家庄': ['新华', '桥西', '长安', '裕华', '矿', '藁城', '鹿泉', '栾城'],
    '廊坊': ['安次', '广阳'],
    '邯郸': ['邯山', '丛台', '复兴', '峰峰矿', '肥乡', '永年', '临漳', '成安', '大名'],
    '无锡': ['梁溪', '锡山', '惠山', '滨湖', '新吴'],
    '徐州': ['云龙', '鼓楼', '泉山', '贾汪', '铜山', '新沂', '睢宁'],
    '杭州': ['上城', '下城', '江干', '拱墅', '西湖', '滨江', '萧山', '余杭', '富阳', '临安', '桐庐', '淳安', '建德'],
    '福州': ['鼓楼', '台江', '仓山', '晋安', '马尾', '长乐'],
    '南昌': ['东湖', '西湖', '青云谱', '青山湖', '湾里', '新建'],
    '九江': ['浔阳', '濂溪', '柴桑', '武宁', '修水', '永修', '德安', '都昌', '湖口', '彭泽', '瑞昌', '共青城', '庐山'],
    '济南': ['市中', '历下', '天桥', '槐荫', '历城', '长清', '章丘', '济阳'],
    '青岛': ['市南', '市北', '黄岛', '崂山', '李沧', '城阳', '即墨', '胶州', '平度'],
    '烟台': ['芝罘', '福山', '牟平', '莱山'],
    '临沂': ['兰山', '罗庄', '河东'],
    '郑州': ['中原', '二七', '管城', '金水', '上街', '惠济', '巩义', '荥阳', '新密', '新郑', '登封', '中牟'],
    '洛阳': ['涧西', '西工', '老城', '洛龙', '吉利', '伊滨'],
    '武汉': ['江岸', '江汉', '沌口', '硚口', '汉阳', '武昌', '青山', '洪山', '东西湖', '汉南', '蔡甸', '江夏', '黄陂'],
    '长沙': ['芙蓉', '天心', '岳麓', '开福', '雨花', '望城'],
    '广州': ['越秀', '东山', '海珠', '荔湾', '番禺', '花都', '从化', '增城'],
    '成都': ['武侯', '锦江', '青羊', '金牛', '成华', '龙泉驿', '温江', '新都', '青白江', '双流', '郫都']
}

client = MongoClient('localhost', 27017)
baidu = client.baidu
phonenum = baidu.phonenum            # 里面是增量的有效手机号，不定时更新数据
company_phone = baidu.company_phone  # 临时的公司-电话数据
coll = baidu.work_1121


def find_phone_from_desc():
    """
        2.1、从职位描述中提取手机号，然后把 公司-手机号 存入 phonenum表中。（主键：公司名称）
    """
    info_list = coll.find()
    for info in info_list:
        # print(info)
        p1 = re.compile(r'\d{11}')
        p2 = re.compile(r'\d{3}-\d{4}-\d{4}')

        phone1_list = p1.findall(info['job_desc'])
        phone2_list = p2.findall(info['job_desc'])
        if phone1_list:
            print(info['company'], phone1_list[0])
            res = phonenum.find({'name': info['company']}).count()
            if not res:
                phonenum.insert_one({'name': info['company'],
                                     'phone': phone1_list[0]})

        elif phone2_list:
            print(info['company'], phone2_list[0])
            res = phonenum.find({'name': info['company']}).count()
            if not res:
                phonenum.insert_one({'name': info['company'],
                                     'phone': phone2_list[0].replace('-', '')})


def get_company_name_to_csv():
    """
        2.2、从数据库中读取“公司名称”字段，去重，写入到company_name.csv文件中
    """
    company_list = []
    job_list = coll.find()
    for info in job_list:
        # print(info['company'])
        if info['company'] not in company_list:
            company_list.append(info['company'])
    # print(company_list)

    with open('company_name.csv', 'w', encoding='utf-8', newline='') as f:
        writer = csv.writer(f, delimiter='\t')
        for company in company_list:
            print(company)
            writer.writerow([company])


def clear_phone_of_company_phone():
    """
        2.4、读取 company_phone(临时表)，对phone进行校验，合法的手机号存入 phonenum
    """
    company_phone_list = company_phone.find()
    for info in company_phone_list:
        # print(info)
        if info['phone'] and info['phone'].replace('-', ''):
            phone = info['phone'].replace('-', '').replace(' ', '')
            if phone and phone[0] == '1' and len(phone) == 11:
                print(info['name'], phone)
                res = phonenum.find({'name': info['name']}).count()
                if not res:
                    phonenum.insert_one({'name': info['company'],
                                         'phone': phone})


def get_company_phone_dict():
    """
        从phonenum表 读取 公司-电话 信息，存入字典company_phone_dict
        key：公司名称， value: 公司电话
    """
    company_phone_dict = {}
    company_phone_list = phonenum.find()
    for info in company_phone_list:
        company_phone_dict[info['name']] = info['phone']
    return company_phone_dict


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
            .replace('回民及提前打路费的勿扰', '').replace('&amp;', '').replace('nbsp;', '').replace('lt;', '').replace('brgt;', '')
    return job_desc


def get_data_of_job():
    """
        三、从数据库中获取招聘数据，根据‘公司名称’去获取公司电话，将数据添加到  job_data_list列表中
    """
    job_data_list = []
    company_phone_dict = get_company_phone_dict()
    job_list = coll.find()

    for info in job_list:
        # print(info)
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
        public_time = info['public_time']  # 采集时间

        row = [company, province, city, district, title, job_desc, detail_address, job_type, release_time, valid_time, salary, require, phone, status, public_time]
        # print(row)
        job_data_list.append(row)

    return job_data_list


def clear_job_data(job_data_list):
    new_job_data_list = []
    for row in job_data_list:
        # print(row)
        row[1] = row[1].replace('省', '')
        row[2] = row[2].replace('市', '')
        row[3] = row[3].replace('区', '')

        if row[3] in row[2]:
            row[3] = random.choice(shiqu_dict.get(row[2]))

        row[4] = '招' + row[7]

        pattern = re.compile(r'([\d-]{8,15})')
        pattern1 = re.compile(r'(.*?岗位职责:?)')
        desc = re.sub(pattern, '', row[5])
        desc = re.sub(pattern1, '', desc)
        desc = desc.replace('&quot;', '').replace('&amp;', '').replace('nbsp;', '').replace('联系方式:', '').replace('联系电话', '')\
                .replace('】', '').replace('\xa0', '').replace('\xa02', '').replace('】', '').replace('龙经理招聘经理：龙经理', '')\
                .replace('quot;', '').replace('\u3000', '').replace('：1', '1')
        if len(desc) < 12:
            desc = ''
        elif '中介' in desc:
            desc = ''
        elif '押金' in desc:
            desc = ''
        if not desc:
            desc = "招%s,要熟练工, 要求有工作经验，无不良嗜好" % row[7]

        row[5] = desc
        row[11] = desc

        row[6] = row[6].replace('工作地点：', '')

        row[12] = re.compile(r'([\d-]{8,15})').findall(row[12])
        if row[12]:
            row[12] = row[12][0]
            if desc and row[12] and len(row[12]) == 11 and '-' not in row[12] and row[12][0] == '1':
                print(row)
                new_job_data_list.append(row)

    return new_job_data_list


def job_data_to_excel(job_data_list):

    # 创建excel工作表
    workbook = xlwt.Workbook(encoding='utf-8')
    worksheet = workbook.add_sheet('sheet1')

    worksheet.write(0, 0, label='公司名称')
    worksheet.write(0, 1, label='所在省')
    worksheet.write(0, 2, label='市')
    worksheet.write(0, 3, label='区县')
    worksheet.write(0, 4, label='工程标题')
    worksheet.write(0, 5, label='工程描述')
    worksheet.write(0, 6, label='详细地址')
    worksheet.write(0, 7, label='工种')
    worksheet.write(0, 8, label='开工时间')
    worksheet.write(0, 9, label='完工时间')
    worksheet.write(0, 10, label='薪酬金额')
    worksheet.write(0, 11, label='接包要求')
    worksheet.write(0, 12, label='手机号')
    worksheet.write(0, 13, label='审核状态')
    worksheet.write(0, 14, label='发布时间')

    for i in range(0, len(job_data_list)):
        worksheet.write(i+1, 0, label=job_data_list[i][0])
        worksheet.write(i+1, 1, label=job_data_list[i][1])
        worksheet.write(i+1, 2, label=job_data_list[i][2])
        worksheet.write(i+1, 3, label=job_data_list[i][3])
        worksheet.write(i+1, 4, label=job_data_list[i][4])
        worksheet.write(i+1, 5, label=job_data_list[i][5])
        worksheet.write(i+1, 6, label=job_data_list[i][6])
        worksheet.write(i+1, 7, label=job_data_list[i][7])
        worksheet.write(i+1, 8, label=job_data_list[i][8])
        worksheet.write(i+1, 9, label=job_data_list[i][9])
        worksheet.write(i+1, 10, label=job_data_list[i][10])
        worksheet.write(i+1, 11, label=job_data_list[i][11])
        worksheet.write(i+1, 12, label=job_data_list[i][12])
        worksheet.write(i+1, 13, label=job_data_list[i][13])
        worksheet.write(i+1, 14, label=job_data_list[i][14])
    workbook.save('OK2.xls')


def main():
    job_data_list = get_data_of_job()
    new_job_data_list = clear_job_data(job_data_list)
    job_data_to_excel(new_job_data_list)


if __name__ == '__main__':
    main()
