import requests
import threading


class ComparePic():

    def __init__(self,key,lists={}):
        self.key = key
        self.lists = lists

    def main(self,urls,i):
        url = "https://aip.baidubce.com/rest/2.0/image-classify/v1/realtime_search/similar/search?access_token=" + self.key

        payload = 'url={}'.format(urls)
        headers = {
            'Content-Type': 'application/x-www-form-urlencoded'
        }
        try:
            response = requests.request("POST", url, headers=headers, data=payload).json()
            scores = response["result"][0]["score"]
            score = round(scores,3)
            dict1[str(i)] = score
            dict2[str(i)] = urls
            print(score)
        except:
            pass

    def res(self):
        global dict1,dict2
        dict1 = {}
        dict2 = {}
        count = 0
        for i in self.lists:
            count += 1
            if count > 6:
                break
            t1 = threading.Thread(target=self.main, args=(self.lists[i], i + 1,))
            t1.start()
            t1.join()

        return dict1, dict2

