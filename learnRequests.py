import requests
def download_image():
    """下载图片，文件"""
    headers = {'user-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.104 Safari/537.36 Core/1.53.2372.400 QQBrowser/9.5.10548.400'}
    url = "http://dealer0.autoimg.cn/dl/10982/newsimg/130364690780019046.jpg"
    response = requests.get(url, headers=headers, stream=True)
    print(response.status_code, response.reason)
    with open('demo.jpg', 'wb') as fd:
        for chunk in response.iter_content(128):
            fd.write(chunk)
# download_image()
def dowload_image_improved():
    """下载图片，关闭流"""
    headers = {'user-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.104 Safari/537.36 Core/1.53.2372.400 QQBrowser/9.5.10548.400'}
    url = "http://dealer0.autoimg.cn/dl/10982/newsimg/130364690780019046.jpg"
    from contextlib import closing
    with closing(requests.get(url, headers=headers, stream=True))as response:
        with open('demo1.jpg', 'wb')as fd:
            for chunk in response.iter_content(128):
                fd.write(chunk)
# dowload_image_improved()
def construct_url(end_point):
    BASE_URL = 'https://api.github.com'
    return '/'.join([BASE_URL, end_point])
def basic_auth():
    """基本认证"""
    response = requests.get(construct_url('user'), auth=('imoocdemo', 'imoocdemo123'))
    print(response.text)
    print(response.request.headers)
    # import base64
    # print(base64.b64decode('aW1vb2NkZW1vOmltb29jZGVtbzEyMw=='))
# basic_auth()
def basic_oauth():
    """oauth认证"""
    # auth = GithubAuth('dd6322fa6c57a548268453dc245cbcdc352a7811')
    headers = {'Authorization': 'token dd6322fa6c57a548268453dc245cbcdc352a7811'}
    response = requests.get(construct_url('user/emails'), headers=headers)
    print(response.request.headers)
    print(response.text)
    print(response.status_code)
import base64
print(base64.b64decode('MNWWFleB0oDmj99B3RRAGQzfmh0=').decode('bs64'))
import requests
import time
def get_data(url):
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 6.2; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2623.87 Safari/537.36"
    }
    html = requests.get(url, headers=headers, timeout=3)
    if html.status_code == 200:
        print(url, '\n', str(time.ctime()))

    else:
        print(url, 'wrong', str(time.ctime()))

if __name__ == '__main__':
    url = 'http://www.example.com'
    get_data(url)
