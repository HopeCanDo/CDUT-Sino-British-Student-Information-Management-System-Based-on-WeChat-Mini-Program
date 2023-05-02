import os
import sys

import requests
import urllib3
from lxml import etree

if __name__ == '__main__':
    urllib3.disable_warnings()
    session = requests.Session()
    url = 'https://student.zy.cdut.edu.cn/user?destination=frontpage-alt'
    username = input("Enter your username:")
    password = input("Enter your password:")
    headers = {
        "Host": "student.zy.cdut.edu.cn",
        "Connection": "keep-alive",
        "Cache-Control": "max-age=0",
        "Upgrade-Insecure-Requests": "1",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36 Edg/110.0.1587.69",
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
        "Sec-Fetch-Site": "same-origin",
        "Sec-Fetch-Mode": "navigate",
        "Sec-Fetch-User": "?1",
        "Sec-Fetch-Dest": "document",
        "sec-ch-ua": "\"Chromium\";v=\"110\", \"Not A(Brand\";v=\"24\", \"Microsoft Edge\";v=\"110\"",
        "sec-ch-ua-mobile": "?0",
        "sec-ch-ua-platform": "\"Windows\"",
        "Referer": "https://student.zy.cdut.edu.cn/user?destination=frontpage-alt",
        "Accept-Encoding": "gzip, deflate, br",
        "Accept-Language": "zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6",
    }
    login = session.get(url=url, headers=headers, verify=False)
    log_html = login.text
    cookies1 = login.cookies
    cookiesA = cookies1.values()[0]
    with open('LoginPage.html', 'w', encoding='utf-8') as fp:
        fp.write(log_html)# This page is login page
    # print(cookiesA)
    tree = etree.HTML(log_html)
    ID = tree.xpath('//*[@id="user-login"]/div/input[1]/@value')[0]
    form_id = tree.xpath('//*[@id="user-login"]/div/input[2]/@value')[0]
    data = {
        'name':  username,
        'pass': password,
        'form_build_id': ID,
        'op': 'Log in',
        'form_id': form_id
    }
    response = session.post(url=url, data=data, headers=headers, allow_redirects=False,verify=False)
    if len(response.cookies.values()) == 0:
        print("Sorry, unrecognized username or password.")
        sys.exit()
    cookies2 = response.cookies
    cookiesB = cookies2.values()[0]
    # print(cookiesB)
    cookies = "tcn1TeS5nGooO="+cookiesA+';'+' SSESSc4a2f09cac52e574e4c5814c37aecde0='+cookiesB
    headers = {
        "Host": "student.zy.cdut.edu.cn",
        "Connection": "keep-alive",
        "Cache-Control": "max-age=0",
        "Upgrade-Insecure-Requests": "1",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36 Edg/110.0.1587.69",
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
        "Sec-Fetch-Site": "same-origin",
        "Sec-Fetch-Mode": "navigate",
        "Sec-Fetch-User": "?1",
        "Sec-Fetch-Dest": "document",
        "sec-ch-ua": "\"Chromium\";v=\"110\", \"Not A(Brand\";v=\"24\", \"Microsoft Edge\";v=\"110\"",
        "sec-ch-ua-mobile": "?0",
        "sec-ch-ua-platform": "\"Windows\"",
        "Referer": "https://student.zy.cdut.edu.cn/user?destination=frontpage-alt",
        "Accept-Encoding": "gzip, deflate, br",
        "Accept-Language": "zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6",
        "Cookie": cookies
    }
    res = session.get(url, headers=headers, verify=False)
    # print(res.status_code)
    with open('.//ceshi.html', 'w', encoding=res.encoding) as f:
        f.write(res.text)
    print("GET "+username+"'s INFO！")
    page_text = res.content
    tree1 = etree.HTML(page_text)
    img_src = tree1.xpath('//*[@id="block-system-main"]/div/div/div[1]/a/img/@src')[0]
    if not os.path.exists('./picLibs'):
        os.mkdir('./picLibs')
    img_name = tree1.xpath('//*[@id="block-system-main"]/div/div/div[1]/a/img/@title')[0] + '.jpg'
    img_data = requests.get(url=img_src, headers=headers,verify=False).content
    img_path = 'picLibs/' + img_name

    if os.path.isfile('./picLibs/'+img_name+'.jpg'):
        print('We already got your picture!')
    else:
        with open(img_path, 'wb') as fp:
            fp.write(img_data)
            print('First to get your picture successfully!')
    chineseName = tree1.xpath('//*[@id="page-title"]/text()')[0]
    nameValue = chineseName.strip()
    print('Chinese Name:'+nameValue)
    studentID = tree1.xpath('//*[@id="block-system-main"]/div/div/div[6]/div[2]/div/text()')[0]
    print('Student ID:'+studentID)

    # score_url = 'https://student.zy.cdut.edu.cn' + tree1.xpath('//*[@id="content"]/div/div[1]/ul/li[9]/a/@href')[0]
    # print(score_url)
    # score_html = session.get(url=score_url,headers=headers,verify=False)
    # print(score_html.status_code)
    # with open('./score.html', 'w',encoding='utf-8') as fp:
    #     fp.write(score_html.text)
    #     print("get score")



