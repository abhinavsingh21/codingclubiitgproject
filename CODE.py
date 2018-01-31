import urllib2
from bs4 import BeautifulSoup

date=raw_input('Enter date in ddmmyy format.\n')

url='http://www.rediff.com/issues/'+date+'hl.html'
page=urllib2.urlopen(url)
soup=BeautifulSoup(page,'html.parser')



div=soup.find('div',attrs={'id':"hdtab1"})

itag=div.find_all('a',attrs={'target':'_new'})

for x in range(1,len(itag)):
    print str(x)+"."+itag[x].text
   
   
    

                   
