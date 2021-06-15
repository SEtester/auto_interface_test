import requests
import jmespath

domain = 'b.kuaidi100.com'


class RequestsOperate:

    def __init__(self, current_case, all_excel_data_list):
        self.current_case = current_case
        self.all_excel_data_list = all_excel_data_list
        self.args_list = self.current_case['get_response_params']

    def get_response(self):
        return self.__send_msg()

    def __send_msg(self):
        print(f"{self.current_case['protocol']}{domain}{self.current_case['path']}")

        response = requests.request(
            method=self.current_case['method'],
            url=f"{self.current_case['protocol']}{domain}{self.current_case['path']}",
            data=eval(self.current_case['data']),
            params=self.current_case['params'],
            cookies=self.current_case['cookies'],
            headers=eval(self.current_case['headers'])
        )


        print('DataCache:', DataCache.__dict__)
        if self.args_list:
            self.get_response_data(response, self.args_list)
        print('DataCache:', DataCache.__dict__)

        return response

    def get_response_data(self, response, response_params):
        for par in eval(response_params):
            # l = ['login_success_001>cookies', 'login_success_001>response_json>.token']
            print(par)
            par_list = par.split('>')
            if len(par_list) == 2 and par_list[1] == 'cookies':
                setattr(DataCache, f'{par_list[0]}_{par_list[1]}', response.cookies.items())

            elif len(par_list) == 3 and par_list[1] == 'response_json':
                value = jmespath.search(par_list[2], response.json())
                setattr(DataCache, f'{par_list[0]}_{par_list[1]}_{"_".join(par_list[2].split("."))}', value)





class DataCache:
    pass
