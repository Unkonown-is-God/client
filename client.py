import requests
from jtalk import jtalk
from julius import Julius
import sys
PREURL = 'https://apitest010.herokuapp.com/'
# this URL is web api URL/<KEY>
if __name__ == "__main__":
    response = str(requests.get(PREURL+'こんばんは'))
    if response == '<Response [503]>':
        print('herokuサーバの無料使用時間を使い切りました、来月までお待ちください')
        sys.exit(1)
    try:
        if sys.argv[1] == 'voice':
            jl = Julius()
            print('なにか喋って')
            flag=1
    except IndexError:
        flag=0
        pass
    while True:
        if flag==1:
            text = jl.load()
            print(text)
            if text == '終わり':
                jl.end()
                break
            elif text == '%NOT FOUND%':
                continue
        else:
            text = input('> ')
            if not text:
                break
        url = PREURL+text
        response = requests.get(url)
        json_data = response.json()
        print(json_data)
        jtalk(json_data['response'])
