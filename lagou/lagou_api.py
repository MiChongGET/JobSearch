import requests
import time
import json
import urllib.request


# 中文转换
def CN2String(str):
    return urllib.request.quote(str)


def main():
    city = input('请输入城市：')
    city = CN2String(city)
    job = input('请输入职位：')
    jobByCN = job
    job = CN2String(job)

    url_start = "https://www.lagou.com/jobs/list_"+job+"?city="+city+"&cl=false&fromSearch=true&labelWords=&suginput="
    url_parse = "https://www.lagou.com/jobs/positionAjax.json?city="+city+"&needAddtionalResult=false"
    headers = {
        'Accept': 'application/json, text/javascript, */*; q=0.01',
        'Referer': 'https://www.lagou.com/jobs/list_'+job+'?city='+city+'&cl=false&fromSearch=true&labelWords=&suginput=',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Safari/537.36'
    }
    for x in range(1, 2):
        data = {
            'first': 'true',
            'pn': str(x),
            'kd': jobByCN
        }
        s = requests.Session()
        s.get(url_start, headers=headers, timeout=3)  # 请求首页获取cookies
        cookie = s.cookies  # 为此次获取的cookies
        response = s.post(url_parse, data=data, headers=headers, cookies=cookie, timeout=3)  # 获取此次文本
        time.sleep(5)
        response.encoding = response.apparent_encoding
        text = json.loads(response.text)
        info = text["content"]["positionResult"]["result"]
        for i in info:
            print(i["companyFullName"])
            companyFullName = i["companyFullName"]
            print(i["positionName"])
            positionName = i["positionName"]
            print(i["salary"])
            salary = i["salary"]
            print(i["companySize"])
            companySize = i["companySize"]
            print(i["skillLables"])
            skillLables = i["skillLables"]
            print(i["createTime"])
            createTime = i["createTime"]
            print(i["district"])
            district = i["district"]
            print(i["stationname"])
            stationname = i["stationname"]
            print('********************')


if __name__ == '__main__':
    main()
