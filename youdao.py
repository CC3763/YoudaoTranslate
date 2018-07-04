import urllib.request
import urllib.parse
import json

content = input("请输入需要翻译的内容：")
url = "http://fanyi.youdao.com/translate?smartresult=dict&smartresult=rule"
data = {}
data['type'] = 'AUTO'
data['i'] = content
data['doctype'] = 'json'
data['xmlversion'] = '2.1'
data['keyfrom'] = 'fanyi.web'
data['ue'] = 'UTF-8'
data['typeresult'] = 'false'
data = urllib.parse.urlencode(data).encode('utf-8')
req = urllib.request.Request(url,data)
req.add_header('Referer','http://fanyi.youdao.com/?keyfrom=dict2.top')
req.add_header('User-Agent','Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36')
response = urllib.request.urlopen(req)
html = response.read().decode('utf-8')
target = json.loads(html)
print("翻译结果：%s" % (target['translateResult'][0][0]['tgt']))
