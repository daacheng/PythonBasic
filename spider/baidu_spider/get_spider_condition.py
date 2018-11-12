import datetime
import csv

"""
get_spider_condition.py功能：
    构造查询条件，保存到"query_condition.csv"文件中，以供后续request请求使用
    [工长, 六枝特区, 县, 20181109, 20181112]
"""


def get_start_end_time(delay):
    """
        获取爬取的起止时间,delay指定范围，比如"三天内","一周内","十天内"
    """
    end_date = str(datetime.datetime.now().strftime('%Y%m%d'))
    start_date = str((datetime.date.today() + datetime.timedelta(days=-3)).strftime("%Y%m%d"))
    return start_date, end_date


def get_query_condition_info(start_date, end_date):
    """
        分别读取 "key.csv","dq.csv"文件，获取查询条件(例：['项目经理', '安乡县', '县'])，保存到列表中
    """
    query_condition_info_list = []
    work_type_list = []
    with open('key.csv', 'r', encoding='utf-8') as f_key:
        reader = csv.reader(f_key)
        for row in reader:
            work_type_list.append(row[0])

    with open('dq.csv', 'r', encoding='utf-8') as f_dq:
        reader = csv.reader(f_dq)
        for row in reader:
            for work_type in work_type_list:
                condition_info = [work_type, row[0], row[1], start_date, end_date]
                # print(condition_info)
                query_condition_info_list.append(condition_info)
    return query_condition_info_list


def main():
    # 一、获取爬取的时间区间,delay指定范围，比如"三天内","一周内","十天内"
    delay = -3
    start_date, end_date = get_start_end_time(delay)
    print(start_date, end_date)

    # 二、获取查询条件("工种","省份")，放到列表中。
    query_condition_info_list = get_query_condition_info(start_date, end_date)

    # 三、将这些"查询条件"写到"query_condition.csv"文件中去
    with open('query_condition.csv', 'w', encoding='utf-8', newline='') as f:
        writer = csv.writer(f, delimiter='\t')
        for query_condition_info in query_condition_info_list:
            writer.writerow(query_condition_info)


if __name__ == '__main__':
    main()