from selenium import webdriver
from time import sleep
import requests as req
import json
from requests_toolbelt.multipart.encoder import MultipartEncoder
import urllib.parse
from os import path

if path.exists("C:\\"):
    driver = webdriver.Firefox(
else:
    driver=webdriver.Firefox(executable_path="/usr/local/bin/geckodriver")
baseUrl='https://www.facebook.com/'
headers={'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:80.0) Gecko/20100101 Firefox/80.0',
           'Referer': 'https://www.facebook.com/',
           'Accept-Language': 'pt-BR,pt;q=0.9',
           'Host': 'www.facebook.com',
           'Connection': 'close',
           'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8'}


def separateCookies(data):
    cookies={}
    for element in data:
        cookies[element["name"]]=element["value"]
    return cookies


def doLogin():
    try:
        print("\033[0;32m[+]\033[0m Starting login.")

        driver.get(baseUrl)
        while 1:
            tam_cookies=len(separateCookies(driver.get_cookies()))
            if tam_cookies >= 6:
                print("\033[0;32m[+]\033[0m Login finished")
                break
                return
    except:
        print("\033[1;31m[+]\033[0m Error on login")
        driver.close()
        exit()


def gettingDtsg():
    try:
        print("\033[0;32m[+]\033[0m Getting fb_dtsg parameter")
        sleep(5)
        page_source=driver.page_source
        cookies=driver.get_cookies()
        cookies=separateCookies(cookies)
        dtsg=page_source.split('["DTSGInitialData",[],{"token":"')
        dtsg=dtsg[1][0:25]
        driver.close()
        print("\033[0;32m[+]\033[0m Successful acquisition of fb_dtsg")
        return dtsg, cookies
    except:
        print("\033[1;31m[+]\033[0m Error on acquisition of fb_dtsg")
        exit()


def gettingGroupList(cookies, dtsg):
    try:
        print("\033[0;32m[+]\033[0m Getting group list")
        data={'fb_dtsg': dtsg, 'fb_api_req_friendly_name':
                'GroupsCometLeftRailResponsiveContainerQuery', 'doc_id': '4755927894477695', "variables": '{"adminGroupsCount":90,"memberGroupsCount":1000,"scale":1      }'}
        r=req.post(baseUrl + 'api/graphql', headers=headers,
                     cookies=cookies, data=data)
        return printGroups(r.text)
    except:
        print("\033[1;31m[+]\033[0m Error on acquisition of group list")
        exit()


def printGroups(groups):
    try:
        groups=json.loads(groups)
        groups=groups['data']['nonAdminGroups']["groups_tab"]["tab_groups_list"]["edges"]
        i=0
        print("\033[0;32m[+]\033[0m Group list:")
        groupsList=[]
        for element in groups:
            print(i, ': ', element['node']['name'])
            i=i + 1
            groupsList.append(
                {'id': element['node']['id'], 'name': element['node']['name']})
        return groupsList
    except:
        print("\033[1;31m[+]\033[0m Error on print group list")
        exit()


def selectGroups(groupsList):
    groups=[]
    text='a'
    while text != "":
        text=input(
            "Enter the number of groups you want to post [Enter to leave]: ")
        groups.append(text)
    del(groups[-1])
    comparegroups=[]
    for item in groups:
        comparegroups.append(groupsList[int(item)])
    return comparegroups


def uploadImagetoStaticServer(cookies, dtsg, image):
    try:
        print("\033[0;32m[+]\033[0m Uploading image to static server")
        url='https://upload.facebook.com/ajax/react_composer/attachments/photo/upload?__a=1&fb_dtsg=' + dtsg
        data=MultipartEncoder(fields={
            'profile_id': cookies['c_user'],
            'source': '8',
            'waterfallxapp': 'comet',
            'farr': ('filename', open(image, 'rb'), 'image/'+image[-3:]),
            'upload_id': 'jsc_c_a0'
        }, boundary='---------------------------368542852711876012201108144481')
        headers['Content-Type']=data.content_type
        r=req.post(url, data=data, headers=headers, cookies=cookies)
        locale=r.text.find('"photoID":"')
        photoID=r.text[locale+11:locale+27]
        print("\033[0;32m[+]\033[0m Image uploaded to the static server")
        return photoID
    except:
        print("\033[1;31m[+]\033[0m Error when uploading image to static server")
        exit()


def connectImageWithPost(cookies, dtsg, variables):
    try:
        print("\033[0;32m[+]\033[0m Connecting image to post")
        data={'__a': '1',
                'fb_dtsg': dtsg,
                'fb_api_caller_class': 'RelayModern',
                'fb_api_req_friendly_name': 'ComposerStoryCreateMutation',
                'variables': variables,
                'doc_id': '4669579913112843'}
        headers['Content-Type']='application/x-www-form-urlencoded'
        r=req.post(baseUrl+'api/graphql/', data=data,
                     cookies=cookies, headers=headers)
        print("\033[0;32m[+]\033[0m Image connected to the post")
        return r.text
    except:
        print("\033[1;31m[+]\033[0m Error connecting image to post")
        exit()


def createVariable(cookies, text, groupID, photoID):
    variables='{"input":{"logging":{"composer_session_id":""},"source":"WWW","attachments":[{"photo":{"id":"'+photoID+'"}}],"message":{"ranges":[],"text":"'+text+'"},"inline_activities":[],"explicit_place_id":"0","tracking":[null],"audience":{"to_id":"'+groupID+'"},"actor_id":"'+cookies +
        '","client_mutation_id":"2"},"displayCommentsFeedbackContext":null,"displayCommentsContextEnableComment":null,"displayCommentsContextIsAdPreview":null,"displayCommentsContextIsAggregatedShare":null,"displayCommentsContextIsStorySet":null,"feedLocation":"GROUP","feedbackSource":0,"focusCommentID":null,"gridMediaWidth":null,"scale":1,"privacySelectorRenderLocation":"COMET_STREAM","renderLocation":"group","useDefaultActor":false,"isFeed":false,"isFundraiser":false,"isFunFactPost":false,"isGroup":true,"isTimeline":false,"isLivingRoom":false,"isSocialLearning":false,"isPageNewsFeed":false,"UFI2CommentsProvider_commentsKey":"CometGroupDiscussionRootSuccessQuery","isDraftGeminiPost":false}'
    return variables
