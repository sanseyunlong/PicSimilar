import requests

class UploadPic():

    def __init__(self,key,url="",image=""):
        self.key = key
        self.url = url
        self.image = image

    def upload(self):
        url = "https://aip.baidubce.com/rest/2.0/image-classify/v1/realtime_search/similar/add?access_token=" + self.key
        if self.url != "" and  self.image == "":
            payload = {"url":self.url,
                       "brief":{"name":"test", "id":"666"}}
        elif self.url == "" and self.image != "":
            payload = {"image": self.image,
                       "brief": {"name":"test", "id":"666"}}
        headers = {'Content-Type': 'application/x-www-form-urlencoded'}
        response = requests.request("POST", url, headers=headers, data=payload).json()
        n = 0
        for i in response:
            n += 1
            if i == "error_code" and response[i] == 216681:
                self.dalete()
                self.upload()
        if n < 4:
            print(response)
            print("图片入库成功！")

    def dalete(self):

        url = "https://aip.baidubce.com/rest/2.0/image-classify/v1/realtime_search/similar/delete?access_token=" + self.key

        if self.url != "" and self.image == "":
            payload = {"url": self.url}
        elif self.url == "" and self.image != "":
            payload = {"image": self.image}
        headers = {
            'Content-Type': 'application/x-www-form-urlencoded'
        }
        response = requests.request("POST", url, headers=headers, data=payload)
        print(response.text)
        print("图片重置成功！")
