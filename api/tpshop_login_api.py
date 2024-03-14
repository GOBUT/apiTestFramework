import requests


class TpshopLoginApi(object):
    # 登录方法
    @classmethod
    def login(cls, data):
        url = "http://192.168.195.171:83/index.php?m=Home&c=User&a=do_login&t=0.28653492334653907"
        respCookies = requests.get(url="http://192.168.195.171:83/index.php?m=Home&c=User&a=verify")
        getCookies = respCookies.cookies
        headers = {'Content-Type': 'application/x-www-form-urlencoded'}
        resp = requests.post(url=url, headers=headers, data=data, cookies=getCookies)
        return resp


if __name__ == '__main__':
    date = {"username": "13812345678", "password": "123456", "verify_code": "8888"}
    resp = TpshopLoginApi.login(date)
    print(resp.json())
