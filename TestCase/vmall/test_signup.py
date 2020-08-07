import allure
import pytest
from Common import Request, Assert, read_excel,Tools

request = Request.Request()
assertions = Assert.Assertions()

# url = 'http://192.168.60.132:1811/'
# excel_list = read_excel.read_excel_list('./document/注册.xlsx')
# ids_list = []
# for i in range(len(excel_list)):
#     # 删除excel_list中每个小list的最后一个元素,并赋值给ids_pop
#     ids_pop = excel_list[i].pop()
#     # 将ids_pop添加到 ids_list 里面
#     ids_list.append(ids_pop)
url = 'http://zhongtai.20783378.com'
head = {}
ids = 0


# @allure.feature('虚拟商城用户模块')
# class Test_user():
#
#     @allure.story("注册接口_成功")
#     def test_signup1(self):
#         signup_resp = request.post_request(url=url + 'user/signup',
#                                            json={"phone": Tools.phone_num(), "pwd": 'aaa123456', "rePwd": 'aaa123456', "userName": Tools.random_str_abc(3)+Tools.random_123(3)})
#         assertions.assert_code(signup_resp.status_code, 200)
#         resp_json = signup_resp.json()
#         assertions.assert_in_text(resp_json['respCode'], '0')
#
#     @allure.story("注册接口")
#     @pytest.mark.parametrize("phone,pwd, rePwd, userName,code",excel_list,ids=ids_list)
#     def test_signup(self,phone,pwd, rePwd, userName,code):
#         signup_resp = request.post_request(url=url + 'user/signup',
#                                             json={"phone": phone, "pwd": pwd, "rePwd": rePwd, "userName": userName})
#         assertions.assert_code(signup_resp.status_code,200)
#         resp_json = signup_resp.json()
#         assertions.assert_in_text(resp_json['respCode'],code)


@allure.feature("获取登录用户信息")
class Test_info():
     @allure.story("登录接口")
     def test_login(self):
        login_resp = request.post_request(url=url + '/api/user/public/pwd/login',
                                          json={"subject": "13800010001", "password": "123456"})

        assertions.assert_code(login_resp.status_code, 200)
        login_resp_json = login_resp.json()
        # 打印响应json
        print(login_resp_json)
        assertions.assert_in_text(login_resp_json['resMsg'], 'success')

        # 提取token
        data_json = login_resp_json['data']

        # # 重新赋值全局变量 head
        global head
        head = {'console-token': data_json['consoleToken']}
        print(head)