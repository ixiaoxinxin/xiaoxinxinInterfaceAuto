#-*- coding: utf-8 -*-
import json
# -*- coding: utf-8 -*-
import requests
import json
url = 'http://api.map.baidu.com/place/v2/search?q=明天生活馆&region=北京&output=json&ak=xkGmf34GBavSLAfI9MgPfii1'
r = requests.get(url) #print r.text
data = r.json()
results = data['results']
print results
for result in results:
#print result['name']
#print result['address']
    print u'名称:{0},地址:{1}'.format(result['name'],result['address'])