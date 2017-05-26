import requests
import re
import pytesseract
from PIL import Image
from PIL import ImageEnhance
from bs4 import BeautifulSoup
from prettytable import PrettyTable
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
# 获取验证码
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
# 识别验证码
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
# 生成课表
def get_classtb(txt):
    soup = BeautifulSoup(txt, "html.parser")
    a = soup.find_all(class_="infolist_common")
    tb = PrettyTable(["课程号", "课程序号", "课程名称", "任课教师", "学分", "选课属性", "考核方式", "考试性质", "是否缓考", "上课时间、地点"])
    tb.padding_width = 1
    # tb.align["课程名称"] = "l" #对齐方式
    for x in range(0, len(a) - 12):
        b = a[x].get_text()  # 处理课表信息
        c = b.split()
        q = c[9: len(c)]
        last_td = ''.join(q)
        td_row = c[0: 9]
        td_row.append(last_td)
        if x == 9:
            td_row[-1] = ' '
            td_row.insert(3, '')
        # print(td_row)
        tb.add_row(td_row)
    return tb

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
        print("第", i, "次登录成功，已登录")
    return postdata
if __name__ == '__main__':
    url_dict = {
        'schoolroll': 'http://202.207.16.237/academic/accessModule.do?moduleId=2060&groupId=', #学籍信息
        'grade': 'http://202.207.16.237/academic/accessModule.do?moduleId=2020&groupId=', #查询成绩
        'classtb': 'http://202.207.16.237/academic/student/currcourse/currcourse.jsdo'#本学期课表
    }
    i = 1
    name = '201420201056'
    passwd = '140181199508181419'
    postdata = login(name, passwd)
    login_page = session.post(url=url_dict['classtb'], data=postdata, headers=headers)
    print("获取本学期课表如下:\n", get_classtb(login_page.text))




