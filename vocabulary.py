# https://www.merriam-webster.com/dictionary/gist
import random
import time

import requests
from bs4 import BeautifulSoup
import re
import sys


def search(s):
    target = 'https://www.vocabulary.com/dictionary/'+s
    req = requests.get(url=target).text
    bf = BeautifulSoup(req, "html5lib")
    texts=bf.find_all('p',class_='short')
    count=0
    if(len(texts)==0):
        getWebster(s)
        return
    for z in str(texts[0].text).split(' '):
        if(count==13):
            print(z)
            count=0
        else:
            print(z+' ',end='')
            count+=1
            # print(z)
    # texts = bf.find_all('p', class_='long')
    # # count=0
    # for z in str(texts[0].text).split(' '):
    #     if (count == 13):
    #         print()
    #         count = 0
    #     else:
    #         print(z + ' ', end='')
    #         count += 1
def getWebster(s):
    # s='shattered'
    target = 'http://www.learnersdictionary.com/definition/'+s
    req = requests.get(url=target).text
    bf = BeautifulSoup(req, "html5lib")
    texts = bf.find_all('div', class_='sblocks')
    if(len(texts)==0):
        getWebster_2(s)
        return
    for z in texts:
        z=z.text
        num = re.sub(r' {2,}', "", str(z))
        num = re.sub(r'\n{4,}', "\n", num)
        for i in num.split('\n'):
            i=i.replace(':','')
            if i != '':
                if i[0]=='[':
                    continue
                if len(i) < 3:
                    print(i, end='')
                else:
                    print(i)
        # print(i.text.replace(' : ',',').replace(':',''))
    # dtText
def getWebster_2(s):
    # s='stygian';
    target = 'https://www.merriam-webster.com/dictionary/' + s
    req = requests.get(url=target).text
    bf = BeautifulSoup(req, "html5lib")
    texts = bf.find_all('span', class_='dtText')
    for z in texts:
        z = z.text
        num = re.sub(r' {2,}', "", str(z))
        num = re.sub(r'\n{4,}', "\n", num)
        for i in num.split('\n'):
            if i=='':continue
            i = i.replace(':', '')
            i = i.replace('  ', ' ')
            count=0
            for z in i.split(' '):
                if (count == 10):
                    print(z)
                    count = 0
                else:
                    print(z + ' ', end='')
                    count += 1
            print(i)
if __name__ == '__main__':
    # getWebster_2('s')
    # search('blast')
    for i in range(14,51):
        print("opening list"+str(i)+".txt")
        temp = sys.stdout
        sys.stdout = open("word_"+str(i)+".txt", "a")
        a=open("List"+str(i)+".txt")
        for i in a.readlines():
            if(i[0].isalpha()==False):
                continue
            time.sleep(random.randint(3,5))
            print(i.replace('\n','')+':')
            temp.write(i)
            search(i.replace('\n',''))
            print('\n----------------------------------')
        sys.stdout.close()
        sys.stdout = temp
        print("finished list"+str(i)+".txt")
        print('\n----------------------------------')
    # print("test sys.stdout")
    # print("test sys.stdout")

