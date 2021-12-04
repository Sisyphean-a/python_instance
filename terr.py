from bs4 import BeautifulSoup
import requests
import bs4

def getHtmlText(url,header):
    r = requests.get(url,headers=header,timeout=30)
    r.encoding = r.apparent_encoding
    a = r.text
    return a 

def findHtmlText(ulist,html):
    soup = BeautifulSoup(html,"lxml")
    lis = soup.select("div.responsive-columns.mclist ul")
    #print(type(list))
    for li in lis :
        print(li.string)

if __name__ == "__main__":
    ulist = []
    header={"user-agent":"Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.79 Safari/537.36"}
    url = "https://terraria.fandom.com/zh/wiki/Terraria_Wiki?variant=zh"
    html = getHtmlText(url,header)
    findHtmlText(ulist,html)