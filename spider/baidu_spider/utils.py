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
    '成都': ['武侯', '锦江', '青羊', '金牛', '成华', '龙泉驿', '温江', '新都', '青白江', '双流', '郫都'],
    '南京': ['玄武', '秦淮', '鼓楼', '建邺', '雨花台', '栖霞', '浦口', '六合', '江宁', '溧水', '高淳'],
    '深圳': ['福田', '罗湖', '南山', '盐田', '宝安', '龙岗', '坪山', '龙华', '光明', '大鹏新'],
    '南宁': ['青秀', '兴宁', '江南', '良庆', '邕宁', '西乡塘', '武鸣'],
    '西安': ['未央', '新城', '碑林', '莲湖', '灞桥', '雁塔', '阎良', '临潼', '长安', '高陵', '鄠邑'],
    '哈尔滨': ['道里', '南岗', '道外', '平房', '松北', '香坊', '呼兰', '阿城', '双城'],
    '大庆': ['萨尔图', '龙凤', '让胡路', '红岗', '大同'],
    '长春': ['南关', '宽城', '朝阳', '二道', '绿园', '双阳'],
    '包头': ['昆都仑', '青山', '东河', '九原', '石拐', '固阳'],
    '连云港': ['海州', '连云', '赣榆', '灌南', '东海', '灌云'],
    '扬州': ['邗江', '广陵', '江都'],
    '南通': ['崇川', '港闸', '通州'],
    '宁波': ['海曙', '江北', '北仑', '镇海', '鄞州', '奉化', '余姚', '慈溪', '象山', '宁海'],
    '温州': ['鹿城', '龙湾', '瓯海', '洞头'],
    '嘉兴': ['南湖', '秀洲', '嘉善', '海盐'],
    '绍兴': ['越城', '柯桥', '上虞', '新昌'],
    '乌鲁木齐': ['天山', '沙依巴克', '新市', '水磨沟', '头屯河', '达坂城', '米东'],
    '绵阳': ['涪城', '游仙', '安州'],
    '贵阳': ['南明', '云岩', '花溪', '乌当', '白云', '观山湖'],
    '遵义': ['红花岗', '汇川', '播州'],
    '昆明': ['五华', '盘龙', '官渡', '西山', '呈贡', '晋宁', '东川', '安宁', '富民', '嵩明', '宜良'],
    '百色': ['田阳', '田东', '平果', '德保', '那坡', '凌云', '乐业', '田林', '西林', '右江'],
    '三亚': ['崖州', '天涯', '吉阳', '海棠'],
    '海口': ['秀英', '龙华', '琼山', '美兰'],
    '常德': ['武陵', '鼎城', '安乡', '汉寿', '桃源', '临澧', '石门'],
    '株洲': ['天元', '芦淞', '荷塘', '石峰', '渌口'],
    '银川': ['兴庆', '西夏', '金凤', '永宁', '贺兰'],
    '赣州': ['章贡', '南康', '大余', '上犹', '崇义', '信丰', '龙南', '定南', '全南', '安远', '宁都', '于都', '兴国', '会昌', '石城', '寻乌'],
    '芜湖': ['镜湖', '弋江', '鸠江', '三山'],
    '合肥': ['蜀山', '瑶海', '庐阳', '包河', '肥西', '庐江'],
    '厦门': ['思明', '湖里', '集美', '海沧', '同安', '翔安'],
    '泉州': ['鲤城', '丰泽', '洛江', '泉港'],
    '淄博': ['张店', '淄川', '博山', '周村', '临淄'],
    '安阳': ['文峰', '北关', '殷都', '龙安'],
    '南阳': ['宛城', '卧龙', '南召', '镇平', '内乡', '淅川', '新野', '唐河', '桐柏', '方城', '西峡', '社旗'],
    '桂林': ['秀峰', '叠彩', '象山', '七星', '雁山', '临桂'],
    '重庆': ['渝中', '万州', '涪陵', '大渡口', '江北', '沙坪坝', '九龙坡', '南岸', '北碚', '綦江', '大足', '渝北', '巴南', '黔江', '长寿', '江津', '合川', '永川'],
    '宝鸡': ['渭滨', '金台', '陈仓'],
    '咸阳': ['秦都', '渭城', '兴平', '彬州', '三原', '泾阳'],
    '兰州': ['城关', '七里河', '西固', '安宁', '红古', '永登'],
    '天水': ['秦州', '麦积', '甘谷', '武山', '秦安'],
    '十堰': ['茅箭', '张湾', '郧阳', '郧西', '竹山', '竹溪', '丹江口'],
    '苏州': ['姑苏', '相城', '吴中', '虎丘', '吴江', '常熟'],
    '宜昌': ['夷陵', '西陵', '伍家岗', '点军', '猇亭'],
    '荆州': ['荆州', '沙市', '江陵', '松滋', '公安'],
    '上海': ['黄浦', '徐汇', '长宁', '静安', '普陀', '虹口', '杨浦', '浦东新', '闵行', '宝山', '嘉定', '金山', '松江', '青浦', '奉贤', '崇明'],
    '常州': ['天宁', '钟楼', '新北', '武进', '金坛', '溧阳']
}

client = MongoClient('localhost', 27017)
baidu = client.baidu
phonenum = baidu.phonenum            # 里面是增量的有效手机号，不定时更新数据
company_phone = baidu.company_phone  # 临时的公司-电话数据
coll = baidu.work_1129


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
                    phonenum.insert_one({'name': info['name'],
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
            .replace('回民及提前打路费的勿扰', '').replace('&amp;', '').replace('nbsp;', '').replace('lt;', '').replace('brgt;', '').replace('联系电话', '')\
            .replace('【', '').replace('】', '').replace('\u200c', '').replace('电话', '').replace('*', '').replace('岗位职责:', '')\
            .replace('1、', '').replace('2、', '').replace('3、', '').replace('4、', '').replace('5、', '') \
            .replace('任职资格:', '').replace('职位要求', '').replace('任职要求', '').replace('职务要求', '').replace('一、', '').replace('二、', '') \
            .replace('三、', '').replace('四、', '').replace('五、', '').replace('工资', '').replace('月工资', '').replace('元', '') \
            .replace('（', '').replace('）', '').replace('/月', '').replace('月薪', '').replace('&quot;', '').replace('&amp;', '')\
            .replace('nbsp;', '').replace('联系方式:', '').replace('联系电话', '')\
            .replace('】', '').replace('\xa0', '').replace('\xa02', '').replace('】', '').replace('工作内容：', '').replace('职位描述:', '')\
            .replace('quot;', '').replace('\u3000', '').replace('1.', '').replace('2.', '').replace('3.', '').replace('4.', '').replace('5.', '') \
            .replace('岗位要求', '').replace('岗位职责：', '').replace('以上', '').replace('1】', '').replace('2】', '').replace('3】', '').replace('4】', '').replace('5】', '')\
            .replace('1．', '').replace('2．', '').replace('3．', '').replace('4．', '').replace('5．', '').replace('职位职责：', '')\
            .replace('①', '').replace('②', '').replace('③', '').replace('招聘岗位：', '').replace('招聘岗位：', '')



    # 去掉描述中的薪资
    pattern = re.compile(r'\d{4,6}')
    job_desc = re.sub(pattern, '', job_desc, count=0, flags=0)
    # print(job_desc)

    return job_desc


def get_data_of_job():
    """
        三、从数据库中获取招聘数据，根据‘公司名称’去获取公司电话，将数据添加到  job_data_list列表中
    """
    job_data_list = []
    company_phone_dict = get_company_phone_dict()
    job_list = coll.find()

    for info in job_list:

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
        release_time = info['release_time']  # 开工时间（当前时间）
        valid_time = info['valid_time']  # 有效时间
        salary = info['salary']  # 有效时间
        require = job_desc  # 职位要求
        status = info['status']  # 状态
        public_time = info['public_time']  # 发布时间

        row = [company, province, city, district, title, job_desc, detail_address, job_type, release_time, valid_time, salary, require, phone, status, public_time]
        print('before:', info['job_desc'])
        print('after:', row[5])
        print('##########################')
        job_data_list.append(row)

    return job_data_list


def clear_job_data(job_data_list):
    new_job_data_list = []
    for row in job_data_list:
        new_row = ['', '', '', '', '', '', '', '', '', '', '', '', '', '', '']
        # print(row)
        new_row[0] = row[0]
        new_row[1] = row[1].replace('省', '')
        new_row[2] = row[2].replace('市', '')
        new_row[3] = row[3].replace('区', '').replace('县', '').replace('市', '')

        if new_row[3] in new_row[2]:
            new_row[3] = random.choice(shiqu_dict.get(new_row[2]))

        if row[4] in ['工长', '电工', '木工', '油漆工', '焊工', '安装工', '水电工', '普工杂工', '工程监理', '工程机械']:
            new_row[4] = '招' + row[7]
        else:
            new_row[4] = row[4]

        pattern = re.compile(r'([\d-]{8,15})')
        pattern1 = re.compile(r'(.*?岗位职责:?)')
        desc = re.sub(pattern, '', row[5])
        desc = re.sub(pattern1, '', desc)
        if len(desc) < 12:
            desc = ''
        elif '中介' in desc:
            desc = ''
        elif '押金' in desc:
            desc = ''
        if not desc:
            desc = "招%s,要熟练工, 要求有工作经验，无不良嗜好" % row[7]

        new_row[5] = desc
        new_row[11] = desc

        new_row[6] = row[6].replace('工作地点：', '')
        new_row[7] = row[7]
        new_row[8] = row[8]
        new_row[9] = row[9]
        new_row[10] = row[10]
        new_row[13] = row[13]
        new_row[14] = row[14]

        new_row[12] = re.compile(r'([\d-]{8,15})').findall(row[12])
        if new_row[12]:
            new_row[12] = new_row[12][0]
            if desc and new_row[12] and len(new_row[12]) == 11 and '-' not in new_row[12] and new_row[12][0] == '1':
                # print(row)
                new_job_data_list.append(new_row)


    # 按照区县、工种、手机号去重
    job_data_dict = {}
    for data in new_job_data_list:
        key = data[3] + data[7] + data[-3]
        key = key.replace(' ', '')
        # print(key)
        job_data_dict[key] = data

    result_list = []
    for k, v in job_data_dict.items():
        print(v)
        result_list.append(v)

    return result_list


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


def to_company_num_csv():
    phone_list = phonenum.find()

    with open('company_phone.csv', 'w', encoding='utf-8', newline='') as f:
        writer = csv.writer(f, delimiter='\t')
        for phone in phone_list:
            writer.writerow([phone['name'], phone['phone']])


def main():
    # 1、从“职位描述”字段中提取手机号，存入phonenum表中
    # find_phone_from_desc()

    # 2、从数据库读取"公司名称"字段，去重，生成company_name.csv文件
    # get_company_name_to_csv()

    # 3、读取company_name.csv文件，通过公司名称，爬取公司电话，存入MongoDB的company_phone表中。(这个表临时存公司-电话信息)  shunqi.py

    # 4、读取 company_phone表中的数据，对手机号进行校验，合格的存入 phonenum 表中。
    # clear_phone_of_company_phone()

    # 5、清洗
    job_data_list = get_data_of_job()
    new_job_data_list = clear_job_data(job_data_list)
    job_data_to_excel(new_job_data_list)
    # to_company_num_csv()

if __name__ == '__main__':
    main()
