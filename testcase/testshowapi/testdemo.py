"""
showapi接口的测试用例
"""
import unittest
from lib.showapi import ShowAPI
import jsonpath
from util.functiontools import assertListEqual

class TestExpress(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.api = ShowAPI()

    def test_64_19(self):
        params = {
            "com": "zhongtong",
            "nu": "75450632975559"
        }
        ret = self.api.send(method="post", path="64-19", params=params)
        self.assertEqual(ret.json()["showapi_res_code"], 0)

    def test_64_20(self):
        params = {
            "expName": "风"
        }
        ret = self.api.send(method="post", path="64-20", params=params)
        print(ret.text)

    def test_64_21(self):
        params = {
            "nu": "SF1163287169821"
        }
        ret = self.api.send(method="post", path="64-21", params=params)
        print(ret.text)
        self.assertEqual(ret.json()["showapi_res_code"], 0)
        self.assertEqual(jsonpath.jsonpath(ret.json(), "$..msg")[0], "操作成功!")
        self.assertEqual(jsonpath.jsonpath(ret.json(), "$..expName").sort(), ["圆通速递","顺丰速运","苏宁快递"].sort())
        self.assertTrue(assertListEqual(jsonpath.jsonpath(ret.json(), "$..expName"), ["圆通速递","顺丰速运","苏宁快递"]))
if __name__ == '__main__':
    unittest.main()