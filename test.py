import requests
import time
from hashlib import md5

url = "https://route.showapi.com/64-19"

#准备参数
params = {
    "showapi_appid": "691912",
    "com": "zhongtong",
    "nu": "75450632975559"
}
#获取当前时间戳
params["showapi_timestamp"] = time.strftime("%Y%m%d%H%M%S")
print(params["showapi_timestamp"])

# 开始拼接字符串
temp = ""
for key in sorted(params):
    temp += key + params[key]

# 加盐
temp += "cf9ff3bbe3ae447c8af90b329b150837"

# 通过md5加密，生成签名，赋值给showapi_sign
params["showapi_sign"] = md5(temp.encode("utf-8")).hexdigest()

print(params)

# 发送接口请求
r = requests.post(url, data=params)

print(r.text)