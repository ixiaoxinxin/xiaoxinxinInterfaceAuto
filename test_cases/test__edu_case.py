#-coding:UTF8-*-
import urllib2,urllib
url = 'http://172.16.7.141:6062/jtsearch/a/ajcxtb/query' #请求的url
data = {'uuid':'12312312445',
        'policyNo':'8603315292016112405',
        'via':'2',
        'inscomp':'0001300041.00004'
        }#根据文档中提供的api参数进行修改
data = urllib.urlencode(data)#给参数编码


#url2 = url + '?' + data
# 跟post不同的只有这一句，使用?把url和data的内容连接起来


url2 = urllib2.Request(url,data)# 用.Request来发送POST请求，指明请求目标是之前定义过的url，请求内容放在data里
response = urllib2.urlopen(url2)# 用.urlopen打开上一步返回的结果，得到请求后的响应内容
apicontent = response.read()#将响应内容用read()读取出来

print apicontent#打印读取到的内容