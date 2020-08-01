import subprocess as sp
import time
import socket
HOST = 'localhost'   # IPアドレス
PORT = 10500         # Juliusとの通信用ポート番号
CMD = './julius/bin/julius -C julius/dic/main.jconf -C julius/dic/am-gmm.jconf -module'
class Julius:
    def __init__(self):
        self.c = sp.Popen(CMD, shell=True,
                          stdout=sp.PIPE, stderr=sp.PIPE)
        #サーバ開始
        self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        while True:
            try:
                self.client.connect((HOST, PORT))
                break
            except ConnectionRefusedError:
                time.sleep(5)
        #接続
        self.data=''
    def end(self):
        print('finished')
        self.client.send("DIE".encode('utf-8'))
        self.client.close()
        #サーバを閉じる
    def load(self):
        if '</RECOGOUT>\n.' in self.data:
            # 出力結果から認識した単語を取り出す
            recog_text = ""
            for line in self.data.split('\n'):
                index = line.find('WORD="')
                if index != -1:
                    line = line[index+6:line.find('"', index+6)]
                    recog_text = recog_text + line
            r=recog_text
            self.data = ""
            return r
        else:
            self.data += str(self.client.recv(1024).decode('utf-8'))
            #見つけた文字列を保存　次回返す
            return '%NOT FOUND%'
            #前回見つけれなかったことを報告
    def demo(self):
        if '</RECOGOUT>\n.' in self.data:
            # 出力結果から認識した単語を取り出す
            recog_text = ""
            for line in self.data.split('\n'):
                index = line.find('WORD="')
                if index != -1:
                    line = line[index+6:line.find('"', index+6)]
                    recog_text = recog_text + line
            print("認識結果: " + recog_text)
            self.data = ""
        else:
            self.data += str(self.client.recv(1024).decode('utf-8'))
if __name__ == "__main__":
    a = Julius()
    print('a')
    try:
        while True:
            a.demo()
    except KeyboardInterrupt:
        a.end()

