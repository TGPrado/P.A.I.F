#!/usr/bin/python3.8
from functions import *
from time import sleep


def main():
    cookies = doLogin()
    dtsg = gettingDtsg(cookies)
    gettingGroupList(cookies, dtsg)


if __name__ == "__main__":
    main()
