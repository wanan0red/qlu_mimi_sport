import json
import random
import re
import time
import jsonpath
import requests
import urllib3
import schedule


token_lsit = ['123456', '789']

def main_fu(youtoken):
    urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
    getline = "https://admin.report.mestallion.com/api/mini/sport/getline"
    map = "https://admin.report.mestallion.com/api/mini/sport/today"
    daka = "https://admin.report.mestallion.com/api/mini/sport/daka"

    header = {
        "User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.143 Safari/537.36 MicroMessenger/7.0.9.501 NetType/WIFI MiniProgramEnv/Windows WindowsWechat",
        "Content-Type": "application/x-www-form-urlencoded",
        "Token": youtoken,
        "Referer": "https://servicewechat.com/wx5069fcccc8151ce3/28/page-frame.html",
    }
    getdata = {
        "lat": "36.55358",
        "lng": "116.75199"
    }

    reqgetline = requests.post(url=getline,headers=header, data=getdata,verify=False)
    jsondata = json.loads(reqgetline.text)
    getcode = jsonpath.jsonpath(jsondata, '$[code]')

    if 200 in getcode:
        print("获取线路成功")
        print(f"页面响应信息:{reqgetline.text}")
    elif 500 in getcode:
        print("获取线路失败")
        print(f"页面响应信息:{reqgetline.text}")

    reqmap = requests.post(url=map, headers=header,verify=False)
    name  = re.findall('"name":"(.{1,12}?)",', reqmap.text)
    print("你好 : " + str(name))
    lngs = re.findall(',"lng":(.{1,12}?),"total_distence":', reqmap.text)
    lats = re.findall(',"lat":(.{9,12}?)}', reqmap.text)
    ids = re.findall(',"id":(.{1,12}?),"lat":', reqmap.text)

    for i in range(4):
        data = {
            "ble": "false",
            "gps": "false",
            "lat": lats[i],
            "lng": lngs[i],
            "bs_id": "",
            "bs_name": "",
            "id": ids[i]
        }
        reqdaka = requests.post(url=daka, headers=header, data=data,verify=False)

        jsondata = json.loads(reqdaka.text)
        code = jsonpath.jsonpath(jsondata, '$[code]')

        if 200 in code:
            print(f"第{i + 1}次打卡成功")
            print(f"页面响应信息:{reqdaka.text}")
        elif 500 in code:
            print(f"第{i + 1}次打卡失败")
            print(f"页面响应信息:{reqdaka.text}")
        time.sleep(330 + random.randint(1, 35))


def start():
    time.sleep(random.randint(1, 35))
    youtoken = token_lsit
    for i in youtoken:
        time.sleep(random.randint(1, 35))
        main_fu(i)


if __name__ == '__main__':

    schedule.every().day.at("17:21").do(start)

    while True:
        time.sleep(0.001)
        schedule.run_pending()