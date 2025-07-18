"""
青龙脚本
mt论坛自动签到
添加变量：mtluntan
账号密码用&隔开
例如账号：1234 密码：1111 则变量为1234&1111
定时规则: 0 0 * * *
需要微信推送请添加变量：PUSH_PLUS_TOKEN
"""
import json
import requests
import re
import os
import time
import notify

# 设置ua
ua = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.45 Safari/537.36'
session = requests.session()

# 签到函数
def main(username,password):
    headers={'User-Agent': ua}
    session.get('https://bbs.binmt.cc/member.php?mod=logging&action=login&infloat=yes&handlekey=login&inajax=1&ajaxtarget=fwin_content_login',headers=headers)
    chusihua = session.get('https://bbs.binmt.cc/member.php?mod=logging&action=login&infloat=yes&handlekey=login&inajax=1&ajaxtarget=fwin_content_login',headers=headers)
    #print(re.findall('loginhash=(.*?)">', chusihua.text))
    loginhash = re.findall('loginhash=(.*?)">', chusihua.text)[0]
    formhash = re.findall('formhash" value="(.*?)".*? />', chusihua.text)[0]
    denurl = f'https://bbs.binmt.cc/member.php?mod=logging&action=login&loginsubmit=yes&handlekey=login&loginhash={loginhash}&inajax=1'
    data = {'formhash': formhash,'referer': 'https://bbs.binmt.cc/forum.php','loginfield': 'username','username': username,'password': password,'questionid': '0','answer': '',}
    denlu = session.post(headers=headers, url=denurl, data=data).text
    #print(denlu)
    if '欢迎您回来' in denlu:
        #获取分组、名字
        fzmz = re.findall('欢迎您回来，(.*?)，现在', denlu)[0]
        print(f'{fzmz}：登录成功')
        #获取formhash
        zbqd = session.get('https://bbs.binmt.cc/k_misign-sign.html', headers=headers).text
        formhash = re.findall('formhash" value="(.*?)".*? />', zbqd)[0]
        #签到
        qdurl=f'https://bbs.binmt.cc/plugin.php?id=k_misign:sign&operation=qiandao&format=text&formhash={formhash}'
        qd = session.get(url=qdurl, headers=headers).text
        qdyz = re.findall('<root><(.*?)</root>', qd)
        print(qdyz)
        login_info = re.findall('欢迎您回来，(.*?)，现在', denlu)[0].strip()
        sign_info = re.findall('<root><(.*?)</root>', qd)[0].strip()
        notify.send('MT论坛签到通知', f'签到信息：{login_info}{sign_info}')
    else:
        print('登录失败')
        notify.send('MT论坛登录失败', '登录失败')

# 从环境变量中读取账号密码
mtluntan = os.getenv("mtluntan")
if mtluntan is not None:
    username, password = mtluntan.split('&')
    main(username,password)
else:
    print('未设置MT论坛账号密码')