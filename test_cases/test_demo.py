import pytest

from utils.excel_handler import ExcelOperate
from utils.requests_handler import RequestsOperate

excel_data_list = ExcelOperate('/Users/dengjiajie/Desktop/my_git/auto_interface_test/datas/接口测试数据表示例.xlsx',
                               'Sheet1').get_excel()


class TestDemo:

    @pytest.mark.parametrize('item', excel_data_list)
    def test_demo(self, item):
        result = RequestsOperate(current_case=item, all_excel_data_list=excel_data_list).get_response()
        print(result.json())
        # print(item, type(item))
        # pass


if __name__ == '__main__':
    pytest.main(['-v', '-s', 'test_demo.py'])
    l = ['login_success_001>cookies', 'login_success_001>response_json>token']
