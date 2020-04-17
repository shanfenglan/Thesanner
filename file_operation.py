import os,time,xlwt

def file_operate(domain1, listt, ipp,feature):
    global sheet_value, first_column, second_column
    domain = domain1

    t = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))

    site = listt
    pwd = str(os.getcwd())
    ip = ipp
    if feature == 'domain':
        feature = 'sub_domain'
        first_column ='subdomain_name'
        second_column = 'IP'
        sheet_value = 'Sub_D and IP'
    elif feature == 'port':
        first_column = 'port'
        second_column = 'status'
        sheet_value = 'port and status'
    elif feature == 'dir_search':
        first_column = 'url'
        second_column = 'status_code'
        sheet_value = 'url and status_code'
    elif feature == 'brute':
        first_column ='brute_subdomain_name'
        second_column = 'IP'
        sheet_value = 'brute_Sub_D and IP'
    elif feature == 'service':
        first_column ='port'
        second_column = 'service'
        sheet_value = 'port and service'
    workbook = xlwt.Workbook(encoding='utf-8')  # 新建工作簿
    sheet1 = workbook.add_sheet(sheet_value)  # 新建sheet
    sheet1.write(0, 0, first_column)  # 第1行第1列数据
    sheet1.write(0, 1, second_column)  # 第1行第2列数据
    hang = 1
    i = 0
    while hang < len(site) + 1:
        sheet1.write(hang, 0, site[i])  # 第2行第1列数据
        sheet1.write(hang, 1, ip[i])  # 第2行第2列数据
        hang += 1
        i += 1
    workbook.save(r'{1}/_output/<{0}>--{2}.xlsx'.format(domain, pwd, feature))  # 保存
    print('[+]The output_file was kept in {1}/_output/<{0}>--{2}.xlsx'.format(domain, pwd, feature))