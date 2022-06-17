import requests
import json
import re


class YqSpider:
    def __init__(self):
        self.url = "https://voice.baidu.com/act/newpneumonia/newpneumonia/?from=osari_pc_3"
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.182 Safari/537.36'
        }

    def parse(self):
        """
        获取数据
        """
        response = requests.get(self.url, headers=self.headers)
        text = response.text # 获取文本信息
        textList = text.split("\n") # 按行分割
        res_str = None
        for text_i in textList:
            res = reMatch("(.*<script>require.config.*)", text_i) # 使用正则表达式匹配出包含“<script>require.config”的行
            if res:
                res_str = res
        summaryDataIn = json.loads(reMatch('.*"summaryDataIn":(.*?}).*', res_str)) # 使用正则表达式获取国内总数
        summaryDataOut = json.loads(reMatch('.*"summaryDataOut":(.*?}).*', res_str)) # 使用正则表达式获取全球总数
        caseList = json.loads(reMatch('.*"caseList":(.*]),"caseOutsideList".*', res_str)) # 使用正则表达式获取国内疫情数据
        caseOutsideList = json.loads(reMatch('.*"caseOutsideList":(.*]),"dataSource".*', res_str)) # 使用正则表达式获取全球疫情数据
        return summaryDataIn, summaryDataOut, caseList, caseOutsideList

def reMatch(reStr, str):
    """
    正则表达式,
    reStr: 正则表达式例如： '.*"caseList":(.*]),"caseOutsideList".*'
    str：文本数据
    """
    matchList = re.match(reStr, str)
    if(matchList):
        return matchList.group(1)
    else:
        return False

if __name__ == '__main__':
    yqSpider = YqSpider()
    yqSpider.parse()
