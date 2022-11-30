import requests


def get_access_token_compare():
    """
    使用 AK，SK 生成鉴权签名（Access Token）
    :return: access_token，或是None(如果错误)
    """
    API_KEY = "xxpfLGqFho9GnGgdW2gKetBj"
    SECRET_KEY = "rLPD3tDT1Vyunf1c4NuSHUm1278Ggrxn"
    url = "https://aip.baidubce.com/oauth/2.0/token"
    params = {"grant_type": "client_credentials", "client_id": API_KEY, "client_secret": SECRET_KEY}
    return str(requests.post(url, params=params).json().get("access_token"))

def get_access_token_ocr():
    API_KEY = 'zt5Ckr8zWzEznAuPerXB727j'
    SECRET_KEY = 'zRonHYozuPQoGazXMwDAt2ItbdY17RaF'
    # client_id 为官网获取的AK， client_secret 为官网获取的SK
    host = 'https://aip.baidubce.com/oauth/2.0/token?grant_type=client_credentials&client_id=' + API_KEY + '&client_secret=' + SECRET_KEY
    response = requests.get(host)
    if response:
        res_dic = response.json()
        token = res_dic['access_token']
        return token
    else:
        print('token获取失败')


