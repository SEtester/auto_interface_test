from pprint import pprint

import xlrd


class ExcelOperate:

    def __init__(self, file_path, sheet_by_name):
        self.file_path = file_path
        self.sheet_by_name = sheet_by_name
        book = xlrd.open_workbook(self.file_path)
        self.sheet = book.sheet_by_name(self.sheet_by_name)

    def get_excel(self):
        """ 获取Excel数据 """
        title = self.sheet.row_values(0)
        l = [dict(zip(title, self.sheet.row_values(row))) for row in range(1, self.sheet.nrows)]
        return l


if __name__ == '__main__':
    excel_data_list = ExcelOperate('/Users/dengjiajie/Desktop/my_git/auto_interface_test/datas/接口测试数据表示例.xlsx',
                                   'Sheet1').get_excel()
    # pprint(excel_data_list)
    # print(excel_data_list[0]['data'], type(excel_data_list[0]['data']))
    print(eval(excel_data_list[0]['data']), type(eval(excel_data_list[0]['data'])))
