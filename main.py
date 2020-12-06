#!/usr/bin/python3.8
from functions import *
from time import sleep


def main():
    cookies = doLogin()
    dtsg = gettingDtsg(cookies)
    groupsList = gettingGroupList(cookies, dtsg)
    selectedgroups = selectGroups(groupsList)
    image = input('Enter the image path: ')
    text = input('Enter the image description: ')
    for group in selectedgroups:
        photoID = uploadImagetoStaticServer(cookies, dtsg, image)


if __name__ == "__main__":
    main()
