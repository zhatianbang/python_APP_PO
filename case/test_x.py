# coding:utf-8
import unittest

class Test_01(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        print("只执行一次")

    def setUp(self):
        print("测试开始的准备工作")

    def test_01(self):
        a = 1
        b = 1
        self.assertTrue(a==b)

    def test_02(self):
        c = 100
        self.assertTrue(c)

    def tearDown(self):
        print("测试结束后的清理工作")

    @classmethod
    def tearDownClass(cls):
        print("只执行一次结束")

if __name__ == "__main__":
    unittest.main()
