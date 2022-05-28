### 制作可视化数据集 ###

from get_data import YqSpider
import pandas as pd
import time


class MakeDataset:
    def __init__(self):
        self.yqSpider = YqSpider()
        self.summaryDataIn, self.summaryDataOut, \
        self.caseList, self.caseOutsideList = self.yqSpider.parse() # 从网页中获取国内疫情数据
        for key in self.summaryDataIn:
            self.summaryDataIn[key] = int(self.summaryDataIn[key])

    def china_dataset(self):
        """
        制作中国地图可视化数据集
        :return:
        """
        # 现有确诊数：[{"云南": 10, "北京": 20, ……}]
        curConfirmData = [{"name": case["area"], "value": case["curConfirm"]} for case in self.caseList]
        # 累计确诊[{"云南": 10, "北京": 20, ……}]
        confirmedData = [{"name": case["area"], "value": case["confirmed"]} for case in self.caseList]

        return self.summaryDataIn, curConfirmData, confirmedData

    def data_to_csv(self, curConfirmData, confirmedData):
        """
        将数据存入csv文件
        """
        data_dict = {'日期':[],'城市':[], '现有确诊':[], '累计确诊':[]} # 初始化存放数据的字典
        date = time.strftime("%Y-%m-%d", time.localtime()) # 获取此时的年月日
        for i in range(len(curConfirmData)):
            data_dict['城市'].append(curConfirmData[i]['name']) # 将全国所有省份的名称，存入到字典中
            data_dict['日期'].append(date) # 将年月日，存入到字典中
            data_dict['现有确诊'].append(curConfirmData[i]['value']) # 将现有确诊，存入到字典中
            data_dict['累计确诊'].append(confirmedData[i]['value']) # 将累计确诊，存入到字典中
        df = pd.DataFrame(data_dict) # 将字典转为 DataFrame格式
        df.to_csv('./yq.csv', index=None, encoding='utf_8_sig') # 将数据存入到csv文件中

if __name__ == '__main__':
    makeDataset = MakeDataset() # 实例化
    summaryDataIn, curConfirmData, confirmedData = makeDataset.china_dataset() # 制作数据集
    makeDataset.data_to_csv(curConfirmData, confirmedData) # 将数据集存入csv
    print("数据已成功存入yq.csv文件")
