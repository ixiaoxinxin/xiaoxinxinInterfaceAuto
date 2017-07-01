#-coding:UTF8-*-
import urllib2,urllib
import unittest, os, sys, time
from tools import HtmlReporter

class Test_Case_1(unittest.TestCase):
    def setUp(self):
        self.url = 'http://172.16.7.141:6062/jtsearch/a/ajcxtb/query'
        self.data = {'uuid': '12312312',
                'policyNo': '8603315292016112405',
                'via': '2',
                'inscomp': '0001300041.00004'
                }
        self.data = urllib.urlencode(self.data)

    def test_error_message_1(self):
        self.url2 = urllib2.Request(self.url, self.data)
        self.response = urllib2.urlopen(self.url2)
        self.apicontent = self.response.read()
        testresult = self.assertIn(self.apicontent,'',msg='pass')
        #print testresult
    def tearDown(self):
        pass

if __name__ == '__main__':
    testunit = unittest.TestSuite()
    testunit.addTest(Test_Case_1("test_error_message_1"))
    report = "E:\\xiaoxinxinInterfaceAuto\\logs\\result.html"
    fp = file(report,"wb")
    runner = HtmlReporter.HTMLTestRunner(stream=fp,title="xiaoxinxin",description="zkx")
    runner.run(testunit)