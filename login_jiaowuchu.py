import requests
import re
import pytesseract
from bs4 import BeautifulSoup
from PIL import Image
from PIL import ImageEnhance
from bs4 import BeautifulSoup
headers = {
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
        'Accept-Encoding': 'gzip, deflate',
        'Accept-Language': 'zh-CN,zh;q=0.8',
        'Connection': 'keep-alive',
        'Content-Length': '0',
        'User-Agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Mobile Safari/537.36',
        'X-Requested-With': 'XMLHttpRequest'
}
session = requests.Session()
loginurl = 'http://202.207.16.237/academic/common/security/login.jsp?login_error=1'
def get_captcha():
    resp = session.get(loginurl).text
    soup = BeautifulSoup(resp, "html.parser")
    pic = soup.find(id="jcaptcha")
    src = re.findall(r"/.+?o", str(pic))
    src = str("http://202.207.16.237/" + src[0])
    r = session.get(src, headers=headers)
    with open('captcha1.JPEG', 'wb')as f:
        f.write(r.content)
        f.close()
    # im = Image.open('captcha1.JPEG')
    # im.show()
    # im.close()
    # captcha = input("please input the captcha\n>")
    captcha = exe_captcha()
    return captcha
def exe_captcha():
    img_name = 'captcha1.jpeg'
    im = Image.open(img_name)
    im = im.resize((160, 50), Image.BILINEAR)#图片放大
    enhancer = ImageEnhance.Color(im)
    enhancer = enhancer.enhance(0)
    enhancer = ImageEnhance.Brightness(enhancer)
    enhancer = enhancer.enhance(2)
    enhancer = ImageEnhance.Contrast(enhancer)
    enhancer = enhancer.enhance(8)
    enhancer = ImageEnhance.Sharpness(enhancer)
    im = enhancer.enhance(10)
    capttxt = pytesseract.image_to_string(im, config='-psm 7')
    x = capttxt.split()
    capttxt = ''.join(x)
    # im.show()
    # print("识别验证码为：", capttxt)
    return capttxt
def login(name, passwd):
    global i
    post_url = "http://202.207.16.237/academic/j_acegi_security_check"
    postdata = {'groupId': '',
                'j_username': '201420201056',
                'j_password': '140181199508181419',
                'j_captcha': '',
                'button1': '%B5%C7%C2%BC'
                }
    postdata['j_captcha'] = get_captcha()
    login_page = session.post(post_url, data=postdata, headers=headers)
    title = login_page.text
    soup = BeautifulSoup(title, "html.parser")
    if soup.title.get_text() != '综合教务管理系统':
        print("第", i, "次识别验证码失败，重新识别")
        i += 1
        login(name, passwd)
    else:
        print("第", i, "次登录成功")
    url1 = 'http://202.207.16.237/academic/accessModule.do?moduleId=2060&groupId='#学籍信息
    url2 = 'http://202.207.16.237/academic/accessModule.do?moduleId=2020&groupId='
    url3 = 'http://202.207.16.237/academic/student/currcourse/currcourse.jsdo'
    getdata = {
        'groupId': '',
        'moduleId': '2000'
    }
    url1_mes = session.get(url3, data=getdata)
    url2_mes = session.get(url2)
    print(url1_mes.text.strip())
    # print(url2_mes.text)
if __name__ == '__main__':
    i = 1
    name = '201420201056'
    passwd = '140181199508181419'
    login(name, passwd)





