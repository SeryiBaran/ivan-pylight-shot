#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import webbrowser
import random
import string


def buildblock(size):
    return ''.join(random.choice(string.ascii_lowercase + string.digits) for _ in range(size))

def open():
    l = buildblock(6)
    while l.startswith('0') == True:
        l.replace('0', buildblock(1))
    url = f"https://prnt.sc/{l}"
    print(url)
    webbrowser.open_new_tab(url)

off = input("Нажми 'Enter' чтобы открыть 3 рандомных скриншота: ")
while off == "":
    open()
    open()
    open()
    off = input("Нажми 'Enter' чтобы открыть 3 рандомных скриншота: ")