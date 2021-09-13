"""
针对showapi的接口调用的方式，进行业务封装
也就是，把签名的固定流程进行封装
"""

from hashlib import md5
import time
from util.client.httpclient import HttpClient
import configparser
import os

class ShowAPI(object):
    """发送showapi平台的接口"""
    API_URL = "https://route.showapi.com"

    def __init__(self, showapi_appid=None, secret_key=None):
        """
        args:
        :param showapi_appid: 服务ID
        :param secret_key:    服务的密钥
        如果实例化时，没有传入参数，就从配置文件中去读取参数
        """
        config = configparser.ConfigParser()
        config_dir = os.path.join(os.path.dirname(os.path.dirname(__file__)), "config")
        print(config_dir)
        config.read(config_dir+"\env.ini", encoding="utf-8")
        if showapi_appid is None:
            self.showapi_appid = config.get("showapi", "SHOWAPI_APPID")
        else:
            self.showapi_appid = showapi_appid
        if secret_key is None:
            self.secret_key = config.get("showapi", "SECRET_ID")
        else:
            self.secret_key = secret_key


    def gen_signature(self, params=None):
        """生成签名信息
        :param params: 请求参数
        :return: 参数签名的md5值
        """
        buff = ""
        for k in sorted(params.keys()):
            buff += str(k) + str(params[k])
        buff += self.secret_key
        return md5(buff.encode("utf-8")).hexdigest()

    def send(self, path, method, params):
        """
        :param path: 接口的路径
        :param method: 接口的请求方法
        :param params: 接口传递的参数
        :return: json
        """
        params["showapi_appid"] = self.showapi_appid
        params["showapi_sign"] = self.gen_signature(params)

        try:
            httpclient = HttpClient()
            url = self.API_URL+'/'+path
            print(params)
            print(url)
            r = httpclient.send_request(method=method, url=url, params_type="form", data=params)
            print(r)
            httpclient.close_session()
            return r
        except Exception as ex:
            print("调用showapi接口失败", str(ex))
