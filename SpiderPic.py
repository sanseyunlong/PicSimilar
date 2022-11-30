import requests
from bs4 import BeautifulSoup
import os
from xpinyin import Pinyin


def urlpic(url,n):
    url = 'http:' + url
    lists[n] = url


def main(ans):
    global lists
    p = Pinyin()
    result1 = p.get_pinyin(ans)
    result = result1.split("-")
    strs = ""
    for i in result:
        strs+=i

    headers = {
        'User-Agent': 'Mozilla/5.0',
        'Referer': 'https://www.vcg.com/',
        'Origin': 'https://www.vcg.com'
    }
    lists = {}
    url = 'https://www.vcg.com/creative-image/{}/'.format(strs)
    r = requests.get(url, headers=headers)
    soup = BeautifulSoup(r.text, 'html.parser')
    list_con_li = soup.find('div', id="imageContent")
    pics = list_con_li.find_all('img')
    s = 0
    n = 0
    dirname = '城市'
    root = os.getcwd()
    path = root + '\\' + dirname
    if not os.path.exists(path):
        os.mkdir(path)
    for pic in pics:
        data_src = pic.get('data-src')
        pic_name = path + '\\' + str(s) + '.jpg'
        urls = str(data_src)
        urlpic(urls, n)
        s += 1
        n += 1
    print('爬取完毕')
    return lists
