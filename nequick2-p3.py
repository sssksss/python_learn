import urllib.request
import urllib.parse

url = 'https://t-ict4d.ictp.it/nequick2/nequick'

headers = {
    'Accept': '*/*',
    'Accept-Language': 'zh-CN,zh;q=0.9',
    'Connection': 'keep-alive',
    'Content-Length': '122',
    'Content-Type': 'application/x-www-form-urlencoded',
    'Cookie': '__utmc=104846213; __utmz=104846213.1526626410.1.1.utmcsr=(direct)|utmccn=(direct)|utmcmd=(none); __utma=104846213.271679078.1526626410.1526626410.1526635035.2; __utmt=1; __utmb=104846213.4.10.1526635035',
    'Host': 't-ict4d.ictp.it',
    'Origin': 'https://t-ict4d.ictp.it',
    'Referer': 'https://t-ict4d.ictp.it/nequick2/nequick-2-web-model',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.181 Safari/537.36',
    'X-Requested-With': 'XMLHttpRequest'
}

post_data = {
    'lat1': 10,
    'lon1': 10,
    'h1': 100,
    'lat2': 20,
    'lon2': 10,
    'h2': 1000,
    'year': 2016,
    'month': 1,
    'day': 15,
    'hour': 10,
    'localtime': 0,
    'user': 0,
    'r12_f': 0,
    'sol_val': 0,
    'itu': 1
}
encode_post = urllib.parse.urlencode(post_data).encode(encoding='utf-8')
request_attr = urllib.request.Request(url=url, data=encode_post, headers=headers)
response = urllib.request.urlopen(request_attr).read().decode('utf-8')
print(response)