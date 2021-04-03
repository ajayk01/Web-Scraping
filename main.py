import requests 
import re
import nltk
import math
from nltk.tag.stanford import StanfordNERTagger
from bs4 import BeautifulSoup 
import json
st = StanfordNERTagger('s/english.all.3class.distsim.crf.ser','s/stanford-ner.jar')
name=[]
place=[]
def hindu_size():
    URL = "https://www.thehindu.com/search/?q=*&order=DESC&sort=publishdate&pd=past-month"
    r = requests.get(URL) 
    soup = BeautifulSoup(r.content, 'html5lib')
    tot = soup.find("div",{"class":"section-controls scrollar-info right hidden-xs"})
    tot=re.sub('<[^>]*>', '', str(tot))
    tot = (tot.replace("\n",""))
    tot=(tot.split("of"))
    tot = (tot[1].split("entries"))[0]
    tot=(int(tot))
    return tot;
def hindu():
    head_lines=[]
    tot = hindu_size()
    print(tot)
    for i in range(20):
        #try:
            URL = "https://www.thehindu.com/search/?q=*&order=DESC&sort=publishdate&pd=past-month&page="+str(i+1)
            print(i+1)
            r = requests.get(URL) 
            soup = BeautifulSoup(r.content, 'html5lib')
            t = soup.findAll("a", {"class": "story-card75x1-text"})
            s = str(t)
            s=re.sub('<[^>]*>', '', s)
            s=(s.split('\n'))
            s.remove('[')
            temp=s[len(s)-1].split("]")
            s[len(s)-1]=temp[0]
            for i in s:
                head_lines.append(i)
                count_name_place(i)
        #except:
            print("error")
            print(len(head_lines))
        
        
    print(len(head_lines))
    return head_lines;
            
        
    

def count_name_place(i):
    for j in nltk.sent_tokenize(i):
            tokens = nltk.tokenize.word_tokenize(j)
            tags = st.tag(tokens)
            for k in tags:
                 if(k[1] in ["PERSON"]):
                     name.append(k[0])
                 elif(k[1] in ["LOCATION"]):
                     place.append(k[0])
    
                     
s=hindu()


name_cap=[]
for i in name:
    name_cap.append(i.upper())

l=[]
name=[]

for i in name_cap:
    if i not in l:
        l.append(i)

for i in l:
    count=[]
    count.append(str(name_cap.count(i)))
    count.append(i)
    name.append(count)
s=(sorted(name,reverse=True))
for i in range(5):
    print(s[i][1] +"=="+s[1][0]+"<br>" )
y={}
for i in range(5):
    x={"count":s[i][0],"name":s[i][1]}
    y[str(i+1)] = x
y = json.dumps(y)

                     
        