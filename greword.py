#!/usr/bin/env python
from bs4 import BeautifulSoup
from requests import get
from random import randrange
import random
import subprocess


def get_word():
    
    url = "https://quizlet.com/18329124/manhattan-gre-advanced-and-essential-combo-word-list-flash-cards/"

    htmldoc = get(url).text
    #Extract the document from the request

    soup = BeautifulSoup(htmldoc,'html.parser')

    wordtags = soup.find_all('span',{'class':'TermText qWord lang-en'})
    meaningtags = soup.find_all('span',{'class':'TermText qDef lang-en'})

    d={}

    for tag,mean in zip(wordtags,meaningtags):
    	d[tag.get_text()]=mean.get_text()

    random_list=list(random.choice(d.items()))

    notifystr = ': '.join(random_list)
    subprocess.Popen(['notify-send',notifystr])

if __name__ == '__main__':
    get_word()
