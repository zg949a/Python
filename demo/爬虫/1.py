import requests
import re
from copyheaders import headers_raw_to_dict
from bs4 import BeautifulSoup
import pandas as pd

def get_html(url, params):
    my_headers = b'''
        accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9
        accept-language: zh-CN,zh;q=0.9
        cache-control: max-age=0
        cookie: x-zp-client-id=448f2b96-6b3a-48e3-e912-e6c8dd73e6cb; adfbid=0; adfbid2=0; Hm_lvt_38ba284938d5eddca645bb5e02a02006=1617108464; sajssdk_2015_cross_new_user=1; sts_deviceid=178832cf3f2680-0b20242883a4a9-6618207c-1296000-178832cf3f3780; sts_sg=1; sts_chnlsid=Unknown; zp_src_url=https%3A%2F%2Fwww.google.com.hk%2F; FSSBBIl1UgzbN7N443S=kc8_mcJe5xsW.UilCMHXpkoWeyQ8te3q7QhYV8Y8aA0Se9k9JJXcnQVvrOJ9NYDP; locationInfo_search={%22code%22:%22538%22%2C%22name%22:%22%E4%B8%8A%E6%B5%B7%22%2C%22message%22:%22%E5%8C%B9%E9%85%8D%E5%88%B0%E5%B8%82%E7%BA%A7%E7%BC%96%E7%A0%81%22}; zp_passport_deepknow_sessionId=a2ea7206sade7641768f38078ea6b45afef0; at=02a0ea392e1d4fd6a4d6003ac136aae0; rt=82f98e13344843d6b5bf3dadf38e8bb2; sensorsdata2015jssdkcross=%7B%22distinct_id%22%3A%221071739258%22%2C%22first_id%22%3A%22178832cf3bd20f-0be4af1633ae3d-6618207c-1296000-178832cf3be4b8%22%2C%22props%22%3A%7B%22%24latest_traffic_source_type%22%3A%22%E7%9B%B4%E6%8E%A5%E6%B5%81%E9%87%8F%22%2C%22%24latest_search_keyword%22%3A%22%E6%9C%AA%E5%8F%96%E5%88%B0%E5%80%BC_%E7%9B%B4%E6%8E%A5%E6%89%93%E5%BC%80%22%2C%22%24latest_referrer%22%3A%22%22%7D%2C%22%24device_id%22%3A%22178832cf3bd20f-0be4af1633ae3d-6618207c-1296000-178832cf3be4b8%22%7D; urlfrom=121126445; urlfrom2=121126445; adfcid=none; adfcid2=none; ZL_REPORT_GLOBAL={%22//www%22:{%22seid%22:%2202a0ea392e1d4fd6a4d6003ac136aae0%22%2C%22actionid%22:%2243ffc74e-c32e-42ee-ba04-1e24611fecde-cityPage%22}}; LastCity=%E4%B8%8A%E6%B5%B7; LastCity%5Fid=538; Hm_lpvt_38ba284938d5eddca645bb5e02a02006=1617111259; zpfe_probe_token=ae612f12s0feb44ac697a7434fe1f22af086; d4d6cd0b4a19fa72b8cc377185129bb7=ab637759-b57a-4214-a915-8dcbc5630065; selectCity_search=538; FSSBBIl1UgzbN7N443T=5pRoIYmxrZTzxVozDFEYjcClKKRpXbK9zf0gYH4zU5AyLqGUMT5fnVzyE0SMv7ZDGFLY0HV8o6iXLPBGBBTJhDhz3TIaQ3omm324Q2m4BSJzD0VgZzesPGIXudf636xQZkuag1QJmdqzgFLv6YPcKq.ukZPymp1IazfsOec5vBcMT9yemSrYb9UBk2XF.rZIeM3mIOBqpNii26kDRzjxHP5TsGLJzWaaZvklHnh61NT4acHPQt3Lq1.w2X4htg9ck.uGhzHt9w954igFEqhLCmggLi9OjPUaiU8TA4yn1oR1T5Qmjm1I5AA0PIu76e0T2u6w2f7thMkv6E7lkoDggrRMta0Z_uVEP3Y1sS8hJw7ycE2PTVtVassRyoN6UuTBHtSZ
        sec-ch-ua: "Google Chrome";v="89", "Chromium";v="89", ";Not A Brand";v="99"
        sec-ch-ua-mobile: ?0
        sec-fetch-dest: document
        sec-fetch-mode: navigate
        sec-fetch-site: same-origin
        sec-fetch-user: ?1
        upgrade-insecure-requests: 1
        user-agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 11_2_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.90 Safari/537.36
        '''
    my_headers = headers_raw_to_dict(my_headers)  # 把复制的浏览器需求头转化为字典形式
    req = requests.get(url, headers=my_headers, params=params)
    req.encoding = req.apparent_encoding
    html = req.text

    return html

# 输入url和城市编号，获取由所有职位信息的html标签的字符串组成的列表：

def get_html_list(url, city_num):

    html_list = list()

    for i in range(1, 12):
        params = {'jl': str(city_num), 'kw': '数据分析师', 'p': str(i)}
        html = get_html(url, params)
        soup = BeautifulSoup(html, 'html.parser')
        html_list += soup.find_all(name='a', attrs={'class': 'joblist-box__iteminfo iteminfo'})

    for i in range(len(html_list)):
        html_list[i] = str(html_list[i])

    return html_list

# 根据上面的HTML标签列表，把每个职位信息的有效数据提取出来，保存csv文件：

def get_csv(html_list):

    # city = position = company_name = company_size = company_type = salary = education = ability = experience = evaluation = list()  #
    # 上面赋值方法在这里是错误的，它会让每个变量指向同一内存地址，如果改变其中一个变量，其他变量会同时发生改变

    # table = pd.DataFrame(columns = ['城市','职位名称','公司名称','公司规模','公司类型','薪资','学历要求','技能要求','工作经验要求'])
    city, position, company_name, company_size, company_type, salary, education, ability, experience = ([] for i in range(9))  # 多变量一次赋值

    for i in html_list:

        if re.search(
                '<li class="iteminfo__line2__jobdesc__demand__item">(.*?)</li> <li class="iteminfo__line2__jobdesc__demand__item">(.*?)</li> <li class="iteminfo__line2__jobdesc__demand__item">(.*?)</li>',
                i):
            s = re.search(
                '<li class="iteminfo__line2__jobdesc__demand__item">(.*?)</li> <li class="iteminfo__line2__jobdesc__demand__item">(.*?)</li> <li class="iteminfo__line2__jobdesc__demand__item">(.*?)</li>',
                i).group(1)
            city.append(s)
            s = re.search(
                '<li class="iteminfo__line2__jobdesc__demand__item">(.*?)</li> <li class="iteminfo__line2__jobdesc__demand__item">(.*?)</li> <li class="iteminfo__line2__jobdesc__demand__item">(.*?)</li>',
                i).group(2)
            experience.append(s)
            s = re.search(
                '<li class="iteminfo__line2__jobdesc__demand__item">(.*?)</li> <li class="iteminfo__line2__jobdesc__demand__item">(.*?)</li> <li class="iteminfo__line2__jobdesc__demand__item">(.*?)</li>',
                i).group(3)
            education.append(s)
        else:
            city.append(' ')
            experience.append(' ')
            education.append(' ')


        if re.search('<span class="iteminfo__line1__jobname__name" title="(.*?)">', i):
            s = re.search('<span class="iteminfo__line1__jobname__name" title="(.*?)">', i).group(1)
            position.append(s)
        else:
            position.append(' ')

        if re.search('<span class="iteminfo__line1__compname__name" title="(.*?)">', i):
            s = re.search('<span class="iteminfo__line1__compname__name" title="(.*?)">', i).group(1)
            company_name.append(s)
        else:
            company_name.append(' ')

        if re.search(
                '<span class="iteminfo__line2__compdesc__item">(.*?) </span> <span class="iteminfo__line2__compdesc__item">(.*?) </span>',
                i):
            s = re.search(
                '<span class="iteminfo__line2__compdesc__item">(.*?) </span> <span class="iteminfo__line2__compdesc__item">(.*?) </span>',
                i).group(1)
            company_type.append(s)
            s = re.search(
                '<span class="iteminfo__line2__compdesc__item">(.*?) </span> <span class="iteminfo__line2__compdesc__item">(.*?) </span>',
                i).group(2)
            company_size.append(s)
        else:
            company_type.append(' ')
            company_size.append(' ')

        if re.search('<p class="iteminfo__line2__jobdesc__salary">([\s\S]*?)<', i):
            s = re.search('<p class="iteminfo__line2__jobdesc__salary">([\s\S]*?)<', i).group(1)
            s = s.strip()
            salary.append(s)
        else:
            salary.append(' ')

        s = str()
        l = re.findall('<div class="iteminfo__line3__welfare__item">.*?</div>', i)
        for i in l:
            s = s + re.search('<div class="iteminfo__line3__welfare__item">(.*?)</div>', i).group(1) + ' '
        ability.append(s)

    table = list(zip(city, position, company_name, company_size, company_type, salary, education, ability, experience))

    return table



if __name__ == '__main__':

    url = 'https://sou.zhaopin.com/'
    citys = {'上海':538, '北京':530, '广州':763, '深圳':765, '天津':531, '武汉':736, '西安':854, '成都':801, '南京':635, '杭州':653, '重庆':551, '厦门':682}
    for i in citys.keys():
        html_list = get_html_list(url, citys[i])
        table = get_csv(html_list)
        df = pd.DataFrame(table, columns=['city', 'position', 'company_name', 'company_size', 'company_type', 'salary',
                                          'education', 'ability', 'experience'])
        file_name = i + '.csv'
        df.to_csv(file_name)
