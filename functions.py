from selenium import webdriver
import getpass
from time import sleep
import requests as req
import json
from requests_toolbelt.multipart.encoder import MultipartEncoder
import urllib.parse
import getpass

driver = webdriver.Firefox(executable_path="/usr/local/bin/geckodriver")
baseUrl = 'https://www.facebook.com/'
headers = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:80.0) Gecko/20100101 Firefox/80.0',
           'Referer': 'https://www.facebook.com/',
           'Accept-Language': 'pt-BR,pt;q=0.9',
           'Host': 'www.facebook.com',
           'Connection': 'close',
           'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8'}


def separateCookies(data):
    cookies = {}
    for element in data:
        cookies[element["name"]] = element["value"]
    return cookies


def gettingCredentials():
    email_credential = input('Enter your e-mail: ')
    passwd_credential = getpass.getpass('Enter your password: ')
    return [email_credential, passwd_credential]


def gettingElements():
    driver.get('https://www.facebook.com')
    email = driver.find_element_by_id("email")
    passwd = driver.find_element_by_id("pass")
    login = driver.find_element_by_id("u_0_b")
    return [email, passwd, login]


def sendData():
    email, passwd, login = gettingElements()
    email_credential, passwd_credential = gettingCredentials()

    email.send_keys(email_credential)
    passwd.send_keys(passwd_credential)
    login.click()


def doLogin():
    try:
        print("\033[0;32m[+]\033[0m Starting login.")
        sendData()
        sleep(2)
        cookies = driver.get_cookies()
        cookies = separateCookies(cookies)
        if cookies['c_user']:
            print("\033[0;32m[+]\033[0m Login finished")
        return cookies
    except:
        print("\033[1;31m[+]\033[0m Login error")
        driver.close()
        exit()


def gettingDtsg(cookies):
    try:
        print("\033[0;32m[+]\033[0m Getting fb_dtsg parameter")
        page_source = driver.page_source
        dtsg = page_source.split('["DTSGInitialData",[],{"token":"')
        dtsg = dtsg[1][0:25]
        driver.close()
        print("\033[0;32m[+]\033[0m Successful acquisition of fb_dtsg")
        return dtsg
    except:
        print("\033[1;31m[+]\033[0m Error on acquisition of fb_dtsg")
        driver.close()
        exit()


def gettingGroupList(cookies, dtsg):
    print("[+] Getting group list")
    data = {'fb_dtsg': dtsg, 'fb_api_req_friendly_name':
            'GroupsCometLeftRailResponsiveContainerQuery', 'doc_id': '2626684824102020', "variables": '{"adminGroupsCount":90,"memberGroupsCount":1000,"scale":1      }'}
    r = req.post(baseUrl + 'api/graphql', headers=headers,
                 cookies=cookies, data=data)
    return printGroups(r.text)


def printGroups(groups):
    groups = json.loads(groups)
    groups = groups['data']["viewer"]["groups_tab"]["tab_groups_list"]["edges"]
    i = 0
    print("[+] Group list:")
    groupsList = []
    for element in groups:
        print(i, ': ', element['node']['name'])
        i = i + 1
        groupsList.append(
            {'id': element['node']['id'], 'name': element['node']['name']})
    return groupsList
