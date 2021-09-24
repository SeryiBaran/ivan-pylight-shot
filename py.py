import webbrowser
import random
import string


def buildblock(size):
    return ''.join(random.choice(string.ascii_lowercase + string.digits) for _ in range(size))

def open():
    url = f"https://prnt.sc/{buildblock(6)}"
    if url.startswith('0') == True:
        url.replace('0', buildblock(1))
    print(url)
    webbrowser.open_new_tab(url)

off = input()
while off == "":
    open()
    open()
    open()
    off = input()