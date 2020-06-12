import requests
PREURL='https://apitest010.herokuapp.com/'
#this URL is web api URL/<KEY>
if __name__ == "__main__":
    while True:
        text=input('> ')
        if not text:
            break
        url=PREURL+text
        response=requests.get(url)
        json_data = response.json()
        print(json_data['response'])

