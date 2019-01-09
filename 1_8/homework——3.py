"""
糗事百科爬虫
https://www.qiushibaike.com/8hr/page/1/

需求：提取每一个帖子里面的用户头像的链接，用户名，段子的内容，点赞数，评论数
文本文件保存
"""
from urllib import request, parse
from lxml import etree
import chardet


def teiba(start_page, end_page):
    headers = {'User-Agent': 'Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Trident/5.0)'}
    url = 'https://www.qiushibaike.com/8hr/page/'
    for i in range(start_page, end_page+1):
        # 请求页面
        new_url = url+str(i)
        req = request.Request(new_url, headers=headers)
        response = request.urlopen(req)
        html = response.read().decode()
        # 页面提取
        html = etree.HTML(html)
        li = html.xpath('//li[contains(@class, "item typs_")]')
        for j in li:
            print('提取中 > > >')
            try:
                # username
                username = j.xpath('.//span[contains(@class, "recmd-name")]/text()')[0]
                # header
                header = 'http:' + j.xpath('.//a[contains(@class, "recmd-user")]/img/@src')[0]
                # dianzan
                dianzan = j.xpath('.//div[contains(@class, "recmd-num")]/span/text()')[0]
                # 评论数
                pinglun = j.xpath('.//div[contains(@class, "recmd-num")]/span/text()')[3]
                with open('./丑事百科.txt', 'a', encoding='utf-8') as f:
                    f.write("用户名:"+username + '\n头像:'+header + '\n点赞数:'+dianzan + '\n评论数:'+ pinglun + '\n'+'*' * 50+'\n')
            except:
                pass


if __name__ == '__main__':
    start_page = int(input('输入起始页'))
    end_page = int(input('输入结束页'))
    teiba(start_page, end_page)
