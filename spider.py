import json
import random
import requests
import csv
import codecs

def 文本_取出中间文本(原文本, 前面的文本, 后面的文本, 开始的位置=0):
    位置_前 = 原文本.find(前面的文本, 开始的位置)
    位置_后 = 原文本.find(后面的文本, 位置_前 + len(前面的文本))
    if 位置_前 != -1 and 位置_后 != -1:
        return 原文本[位置_前 + len(前面的文本):位置_后]
    else:
        return ''

def writeJson(file_name, str):
    with open(file_name, 'w') as f:
        f.write(str)

def reqJson(url):
    headers = {}
    user_agent_list = [
        "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36",
        "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36",
        "Mozilla/5.0 (Windows NT 10.0; WOW64) Gecko/20100101 Firefox/61.0",
        "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.186 Safari/537.36",
        "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.62 Safari/537.36",
        "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.101 Safari/537.36",
        "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.0)",
        "Mozilla/5.0 (Macintosh; U; PPC Mac OS X 10.5; en-US; rv:1.9.2.15) Gecko/20110303 Firefox/3.6.15",
    ]
    headers['User-Agent'] = random.choice(user_agent_list)
    req = requests.get(url, headers=headers)
    return req.text

def getInfoSingle(typeofdata):
    """
    拼接数据URL获取不同类型数据
    :param typeofdata: 数据类型，0.简答、1.填空、2.单选、3.多选、4.判断
    :param index: 数据页的索引
    """
    urls = []
    for i in range(1,datapages[typeofdata] + 1):
        urls.append(urlbase + "/data/" + datatype[typeofdata] + '_' + str(i) + '.json')
    return urls

def getInfoAll():
    for i in range(5):
        urls = getInfoSingle(i)
        dict = ''
        for p in urls:
            text = reqJson(p)
            dict += 文本_取出中间文本(text,'[',']') + ','
        dict = '[' + dict[0:len(dict)-1] + ']'
        writeJson(datatype[i].split('/')[-1] + '.json', json.dumps(json.loads(dict), ensure_ascii=False))

if __name__ == '__main__':
    #print(文本_取出中间文本('[{"id":"211","question":"地震破坏最严重的地区叫( )。","answer":"极震区"},{"id":"212","question":"与地震的发生相伴且有成因联系的地面或低空自然发光现象叫( )。","answer":"地光"}]','[',']'))
    #exit(1)
    urlbase = 'http://gjaqjs.haedu.cn'
    # $.getJSON('./data/' + url + '_' + index + '.json', function(res)
    datatype = ['gjaqzsjsxxzl_jianda/gjaqzsjsxxzl_jianda', 'gjaqzsjsxxzl_tiankong/gjaqzsjsxxzl_tiankong',
                'gjaqzsjsxxzl_danxuan/gjaqzsjsxxzl_danxuan', 'gjaqzsjsxxzl_duoxuan/gjaqzsjsxxzl_duoxuan',
                'gjaqzsjsxxzl_panduan/gjaqzsjsxxzl_panduan']
    datapages = [6,8,16,9,11]
    datatotal = [158,212,467,243,316]

    getInfoAll()
