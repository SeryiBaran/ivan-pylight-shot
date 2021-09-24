import webbrowser
import random
import string


def buildblock(size):
    return ''.join(random.choice(string.ascii_lowercase + string.digits) for _ in range(size))

def open():
    url = f"https://prnt.sc/{buildblock(6)}"
    print(url)
    webbrowser.open_new_tab(url)
    url = f"https://prnt.sc/{buildblock(6)}"
    print(url)
    webbrowser.open_new_tab(url)
    url = f"https://prnt.sc/{buildblock(6)}"
    print(url)
    webbrowser.open_new_tab(url)

off = input()
while off == "":
    open()
    off = input()