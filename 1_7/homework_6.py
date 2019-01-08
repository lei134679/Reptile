"""
6、从西刺网查找代理ip，通过代理ip爬取腾讯首页，打印爬取内容
"""
from urllib import request
import chardet
headers = {'User-Agent':'Mozilla/5.0 (compatible; WOW64; MSIE 10.0; Windows NT 6.2)'}
# 定义代理ip
porxy = {'http':'221.233.198.142:50295'}
# 定义代理处理器对象
porxy_handler = request.ProxyHandler(porxy)
# 创建opener对象
opener = request.build_opener(porxy_handler)
# 使用UserAgent
opener.addheaders = {('User-Agent', 'Mozilla/5.0 (compatible; WOW64; MSIE 10.0; Windows NT 6.2)')}
# 安装opener
request.install_opener(opener)

# response = request.urlopen('https://www.qq.com/')
# html = response.read()
# char = chardet.detect(html)['encoding']
# print(char)
# html = html.decode(char)
# print(html)
import zlib
url='https://www.qq.com/'
req = request.Request(url)
response = request.urlopen(req, timeout=120)
html = response.read()
encoding = response.info().get('Content-Encoding')
print(encoding)
if encoding == 'gzip':
    html = zlib.decompress(html, 16+zlib.MAX_WBITS)
elif encoding == 'deflate':
    try:
        html = zlib.decompress(html, -zlib.MAX_WBITS)
    except zlib.error:
        html = zlib.decompress(html)

charset = chardet.detect(html)["encoding"]
print(charset)
#print(html)
print(html.decode(charset,'ignore'))
