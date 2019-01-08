"""
5、批量爬取贴吧数据
输入贴吧名称， 起始页码， 结束页码， 爬取贴吧数据， 以‘第x页.html’
 命名， 保存为html 文件
"""
from urllib import request, parse
import chardet
url = 'http://tieba.baidu.com/f?'
# 拼接名字
url_kw = {"kw":input('输入贴吧名称')}
url_kw = parse.urlencode(url_kw)
# 拼接编码
url_ie = {'ie': 'utf-8'}
url_ie = parse.urlencode(url_ie)
# 拼接页码
start_page = input('起始页码')
end_page = input('结束页码')
for i in range(int(start_page),int(end_page)):
    url_pn = {'pn': i*50}
    url_pn = parse.urlencode(url_pn)
    new_url = ('%s&%s&%s&%s'%(url, url_kw, url_ie, url_pn))
    # 请求页面
    headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36'}
    req = request.Request(new_url, headers=headers)
    resposer = request.urlopen(req)
    html = resposer.read()
    char = chardet.detect(html)['encoding']
    html = html.decode(char, 'ignore')
    with open('d:/第%s页.html'%i,'w',encoding='utf8') as f:
        f.write(html)

