#coding: utf-8
import subprocess


def jtalk(t):
    open_jtalk = ['open_jtalk']
    mech = ['-x', '/var/lib/mecab/dic/open-jtalk/naist-jdic']
    htsvoice = ['-m', 'voice/mei_normal.htsvoice']
    speed = ['-r', '1.0']
    outwav = ['-ow', 'open_jtalk.wav']
    cmd = open_jtalk+mech+htsvoice+speed+outwav
    c = subprocess.Popen(cmd, stdin=subprocess.PIPE,
                         stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    c.stdin.write(t.encode())
    c.stdin.close()
    c.wait()
    aplay = ['aplay', '-q', 'open_jtalk.wav']
    wr = subprocess.Popen(aplay)

if __name__ == "__main__":
    jtalk('お前はすでに死んでいる')
