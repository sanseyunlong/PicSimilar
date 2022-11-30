import requests

def img_info(id,url):
    try:
        img_data = requests.get(url)
    except:
        pass
        # 保存图片
    img_path = "./static/downloads/" + str(id)+".jpg"
    with open(img_path, 'wb') as fp:
        fp.write(img_data.content)
