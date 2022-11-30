import requests
import base64
import Key
'''
通用物体和场景识别
'''
def pic_sb1(filePath):
    request_url = "https://aip.baidubce.com/rest/2.0/image-classify/v2/advanced_general"
    # 二进制方式打开图片文件
    f = open(filePath, 'rb')
    image = base64.b64encode(f.read())
    params = {"image": image}
    access_token = Key.get_access_token_ocr()
    request_url = request_url + "?access_token=" + access_token
    headers = {'content-type': 'application/x-www-form-urlencoded'}
    response = requests.post(request_url, data=params, headers=headers)
    if response:
        images = response.json()
        per = images['result'][0]['score'] * 100
        ans = images['result'][0]['keyword']
        print("相似度：%s%%" % per)
        print("识别结果：%s" % ans)
        return image,ans

# 需要识别的本地图片

