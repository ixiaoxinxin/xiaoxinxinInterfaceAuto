#-coding:UTF8-*-
import urllib2,urllib
import unittest

class Test_Case_1(unittest.TestCase):
    def setUp(self):
        self.url = 'http://172.16.7.141:6062/jtsearch/a/ajcxtb/query'
        self.data = {'uuid': '12312312',
                'policyNo': '8603315292016112405',
                'via': '2',
                'inscomp': '0001300041.00004'
                }
        self.data = urllib.urlencode(self.data)

    def error_message_1(self):
        self.url2 = urllib2.Request(self.url, self.data)
        self.response = urllib2.urlopen(self.url2)
        self.apicontent = self.response.read()
        testresult = self.assertIn(self.apicontent,'',msg='pass')
        #print testresult
    def tearDown(self):
        pass



