from bs4 import BeautifulSoup
from requests import get
from random import randrange

#Generating request for the specific url ###
url = "https://quizlet.com/58647605/kaplan-900-flash-cards/"

htmldoc = get(url).text
#Extract the document from the request###

soup = BeautifulSoup(htmldoc,'html.parser')
# soup is object of BeautifulSoup

wordtags = soup.find_all('span',{'class':'TermText qWord lang-en'})
meaningtags = soup.find_all('span',{'class':'TermText qDef lang-en'})

words = []
meanings = []

for tag in wordtags:
    words.append(tag.get_text())

for tag in meaningtags:
    meanings.append(tag.get_text())

index = randrange(0,len(words))
print "The word choosen is " + words[index] + " : " + meanings[index]
