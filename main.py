#!/usr/bin/python3.8
from functions import *
from time import sleep


def main():
    cookies = doLogin()
    dtsg = gettingDtsg(cookies)
    groupsList = gettingGroupList(cookies, dtsg)
    selectGroups(groupsList)


if __name__ == "__main__":
    main()
