# coding=utf-8

import http.client
import hashlib
import urllib
import random
import json

appid = '20200409000414647'
secretKey = 'PwWp82YEZKiCflazFZPh'

httpClient = None
myurl = '/api/trans/vip/fieldtranslate'

fromLang = 'zh'
toLang = 'en'
q = "耗尽层"
salt = random.randint(32768, 65536)
domain = 'electronics'
sign = appid + q + str(salt) + domain + secretKey
sign = hashlib.md5(sign.encode()).hexdigest()
myurl = myurl + '?appid=' + appid + '&q=' + urllib.parse.quote(q) + '&from=' + fromLang + '&to=' + toLang + '&salt=' +str(salt) + '&domain=' + domain +  '&sign=' + sign

try:
    httpClient = http.client.HTTPConnection('api.fanyi.baidu.com')
    httpClient.request('GET', myurl)


    response = httpClient.getresponse()
    result_all = response.read().decode("utf-8")
    result = json.loads(result_all)

    print (result['trans_result'][0]['dst'])

except Exception as e:
    print (e)
finally:
    if httpClient:
        httpClient.close()
