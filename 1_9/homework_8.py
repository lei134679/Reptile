"""
1、知网爬虫
https://www.cn-ki.net/
搜索“人工智能”，提取搜索结果中论文标题，作者，链接，媒体期刊
数据保存到mysql数据库中
https://search.ehn3.com/search?keyword=%E4%BA%BA%E5%B7%A5%E6%99%BA%E8%83%BD&db=SCDB
"""
from urllib import parse
from lxml import etree
import requests
from sqlalchemy import create_engine
url = 'https://search.ehn3.com/search?'
# name = {'keyword': input('输入搜索内容')}
# name = parse.urlencode(name)
new_url = url + 'keyword=%E4%BA%BA%E5%B7%A5%E6%99%BA%E8%83%BD' + '&db=SCDB'
req = requests.get(new_url)
html = etree.HTML(req.text)
ls = html.xpath('//div[contains(@class, "mdui-col-xs-12 mdui-col-md-9 mdui-typo")]')
base_url = 'https://search.ehn3.com'
for i in ls:
    # title
    title = i.xpath('./h3/a//text()')
    tit = ''.join(title)
    # author
    author = i.xpath('.//span[contains(@class, "mdui-text-color-green-700")]/text()')[0]
    # link
    link = base_url+i.xpath('./h3/a/@href')[0]
    # date
    date = i.xpath('.//span[contains(@class, "mdui-text-color-green-700")]/text()')[-2]
    # kan
    kan = i.xpath('.//span[contains(@class, "mdui-text-color-green-700")]/text()')[1]
    # 存入mysql
    engin = create_engine('mysql+mysqlconnector://root:123456@localhost/reptile_rgzn')
    result = engin.execute('insert into rgzn values(0, "%s", "%s", "%s", "%s", "%s")'%(tit, author, link, date, kan))


