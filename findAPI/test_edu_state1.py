#-*- coding: utf-8 -*-
import json
# -*- coding: utf-8 -*-
import requests
import json
url = 'http://10.30.131.76:6062/jtsearch/a/ajcxtb/query?uuid=123456&policyNo=011262981703040A000026&via=2&' \
      'inscomp=0001300041.00004'
r = requests.get(url) #print r.text
data = r.json()
results = data['results']
print results
for result in results:
#print result['name']
#print result['address']
    print u'名称:{0},地址:{1}'.format(result['uuid'],result['policyNo'],result['via'],result['inscomp'])