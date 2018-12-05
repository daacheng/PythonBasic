import csv
import os


def clear_company_url():
    # base_dir中每一个 .csv文件都是一个行业分类，里面每一条数据都是 [公司名称，公司url]
    base_dir = r'E:\code\PythonBasic\spider\shunqi_spider\company'
    cvt_dir = r'E:\code\PythonBasic\spider\shunqi_spider\company_after_clear'
    all_files_list = []
    # 遍历文件夹下所有文件
    for root, dirs, files in os.walk(base_dir):
        for file in files:
            all_files_list.append(os.path.join(root, file))

    for filepath in all_files_list:
        name = os.path.split(filepath)[1]
        cvt_filepath = os.path.join(cvt_dir, name)
        print('(%s),(%s)' % (filepath, name))
        with open(filepath, 'r', encoding='utf-8') as fr:
            with open(cvt_filepath, 'w', encoding='utf-8', newline='') as fw:
                reader = csv.reader(fr)
                writer = csv.writer(fw)
                for row in reader:
                    if '商铺' in row[0]:
                        continue
                    if '公司' not in row[0]:
                        print(row[0])
                        continue

                    new_row = [row[0], row[1].replace('http:////', 'http://')]
                    writer.writerow(new_row)


def assort_error_url_file():
    """

        error_url.csv文件中提取出，表示公司行业分类的url
    """
    detail_category_url_dict = {}
    with open('detail_category.csv', 'r', encoding='utf-8') as fr:
        reader = csv.reader(fr)
        for row in reader:
            detail_category_url_dict[row[0]] = row[1]

    with open('error_url.csv', 'r', encoding='utf-8') as f_err:
        reader = csv.reader(f_err)
        for row in reader:
            print(row)
            if row[0] in detail_category_url_dict.values():
                print(row)


def main():
    clear_company_url()


if __name__ == '__main__':
    main()