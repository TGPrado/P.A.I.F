#!/usr/bin/python3.8
from functions import *
from time import sleep


def main():
    doLogin()
    dtsg, cookies = gettingDtsg()
    groupsList = gettingGroupList(cookies, dtsg)
    selectedgroups = selectGroups(groupsList)
    image = input('Enter the image path: ')
    text = input('Enter the image description: ')
    for group in selectedgroups:
        photoID = uploadImagetoStaticServer(cookies, dtsg, image)
        variables = createVariable(
            cookies['c_user'], text, group['id'], photoID)
        postresponse = connectImageWithPost(cookies, dtsg, variables)
        url = 'https://www.facebook.com/photo/?fbid='+photoID
        print('\033[0;32m[+]\033[0m The url for the image in, ',
              group['name'], ' is: ', url)
        sleep(6)


if __name__ == "__main__":
    main()
