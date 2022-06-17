import requests
import re
from copyheaders import headers_raw_to_dict
from bs4 import BeautifulSoup
import pandas as pd


# 根据url和参数获取网页的HTML：

def get_html(url, params):

    my_headers = b'''
    Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9
    Accept-Encoding: gzip, deflate, br
    Accept-Language: zh-CN,zh;q=0.9
    Cache-Control: max-age=0
    Connection: keep-alive
    Cookie: x-zp-client-id=448f2b96-6b3a-48e3-e912-e6c8dd73e6cb; sts_deviceid=178832cf3f2680-0b20242883a4a9-6618207c-1296000-178832cf3f3780; Hm_lvt_38ba284938d5eddca645bb5e02a02006=1624877846; urlfrom2=121114584; adfcid2=www.google.com; adfbid2=0; FSSBBIl1UgzbN7NO=5QbLj2_L5kKhv8gnuJa.E1._8RKksG1y5Nt4FRrSajQ7PKGJ8CcWopqTuOLay__ida1esO2ud4AdXKKDI69j9UA; locationInfo_search={%22code%22:%22538%22%2C%22name%22:%22%E4%B8%8A%E6%B5%B7%22%2C%22message%22:%22%E5%8C%B9%E9%85%8D%E5%88%B0%E5%B8%82%E7%BA%A7%E7%BC%96%E7%A0%81%22}; selectCity_search=538; ssxmod_itna=7qGxnDRG0=KGqAKGHKiQRSDQwKfkKqYteb87Dla=xA5D8D6DQeGTb0NpYeYietdigMWPqKYG4iteiFlYfPtb+4OEdD84i7DKqibDCqD1D3qDkbCYxiinDCeDIDWeDiDG+8D0hXl7DjQNXZKkULfBNDz4X2/4UgQDDHfG024dLRIqIgFA+5HYbDbxp9DB6rxBQ/Iqj6znUDgMTTibwbj8DoGiP=fifwn7Dq0YoYCA44fDx=bb4ee2hso7DYFDqojR8DG4xL2iD===; ssxmod_itna2=7qGxnDRG0=KGqAKGHKiQRSDQwKfkKqYteb8D61Fgj40y4rP03aKenjt6D6QMTiBeG2Yn408DewGD; urlfrom=121114584; adfcid=www.google.com; adfbid=0; sts_sg=1; sts_chnlsid=Unknown; zp_src_url=https%3A%2F%2Fwww.google.com.hk%2F; LastCity=%E4%B8%8A%E6%B5%B7; LastCity%5Fid=538; sensorsdata2015jssdkcross=%7B%22distinct_id%22%3A%221071739258%22%2C%22first_id%22%3A%22178832cf3bd20f-0be4af1633ae3d-6618207c-1296000-178832cf3be4b8%22%2C%22props%22%3A%7B%22%24latest_traffic_source_type%22%3A%22%E8%87%AA%E7%84%B6%E6%90%9C%E7%B4%A2%E6%B5%81%E9%87%8F%22%2C%22%24latest_search_keyword%22%3A%22%E6%9C%AA%E5%8F%96%E5%88%B0%E5%80%BC%22%2C%22%24latest_referrer%22%3A%22https%3A%2F%2Fwww.google.com%2F%22%7D%2C%22%24device_id%22%3A%22178832cf3bd20f-0be4af1633ae3d-6618207c-1296000-178832cf3be4b8%22%7D; acw_tc=276082a716357771539376802e2983bc8a5c6ad6d09a856f4d30d3892a3cd8; 1420ba6bb40c9512e9642a1f8c243891=68d62e0e-9c02-4c51-b5be-268470d6b21e; d4d6cd0b4a19fa72b8cc377185129bb7=1e7229ad-ee24-4063-9e4b-6522acfeefc7; at=01e2bf60daa14c479e524b22cfaf306f; rt=0747ac22bd424c8da3c28cb6bbd7a8f6; zpfe_probe_token=3d5af381s32ee94285a4e785bfcdba4df809; FSSBBIl1UgzbN7NP=53Ud_uDmd57aqqqmZC5Xn3qKkeoR73_UtjtoQEvodODN_.CWXzEhTjq8aUd0_FtFCmJ7zHbxzlDmsdsmVKETzSt0C8oeOyH7oQmVQMzAfCehTWeQ6QfajFpiObY8ukPfhc73vMi1pSbFiE4Iu4rGZjz8L_8Ww80.iFXTkrYYJ.C4nZ1OPCmdGhgVIZBVau1P0P1.qTYIvWuWSQyPdlNvBFfVCjF4x0XIP4AL9VK0E4YZZzV54JqXOXzFr6ox5zzXRW4NTRXe_iYnJ0B7XRWx07n
    Host: sou.zhaopin.com
    Referer: https://sou.zhaopin.com/
    sec-ch-ua: "Google Chrome";v="95", "Chromium";v="95", ";Not A Brand";v="99"
    sec-ch-ua-mobile: ?0
    sec-ch-ua-platform: "macOS"
    Sec-Fetch-Dest: document
    Sec-Fetch-Mode: navigate
    Sec-Fetch-Site: same-origin
    Sec-Fetch-User: ?1
    Upgrade-Insecure-Requests: 1
    User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.69 Safari/537.36
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

    url = 'https://zhipin.com/'
    citys = {'上海':538, '北京':530, '广州':763, '深圳':765, '天津':531, '武汉':736, '西安':854, '成都':801, '南京':635, '杭州':653, '重庆':551, '厦门':682}
    for i in citys.keys():
        html_list = get_html_list(url, citys[i])
        table = get_csv(html_list)
        df = pd.DataFrame(table, columns=['city', 'position', 'company_name', 'company_size', 'company_type', 'salary',
                                          'education', 'ability', 'experience'])
        file_name = i + '.csv'
        df.to_csv(file_name)


