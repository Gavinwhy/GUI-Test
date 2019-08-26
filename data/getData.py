import xlrd

from WBossGUITest.common.Setup import Setup
# from WBossGUITest.common.main_login import Login


# 获取数据 - 01
# 从测试用例文件,casedata.xlsx 读取数据
def get_data():
    # 用例路径
    path = "./casedata.xlsx"
    #初始数据
    data = []
    book = xlrd.open_workbook(path)
    sheet = book.sheets()[0]
    # 取每行数据
    for i in range(1, sheet.nrows):
        li = sheet.row_values(i)
        data.append(li)
    # print(data)
    return data

