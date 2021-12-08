from bs4 import BeautifulSoup
import requests
import bs4
from requests import models

def getHtmlText(url,header):
    r = requests.get(url,headers=header,timeout=30)
    r.encoding = r.apparent_encoding
    a = r.text
    return a 

def getUrlList(ulist,html):
    pass


def DownHtmlText(ulist,html,findPash):
    soup = BeautifulSoup(html,"lxml")
    lis = soup.select("div#main-section div.")
    print(len(lis))
    for li in lis :
        print(li["class"])

def Downloadfild(t,findPash):
    with open(findPash,"a",encoding='utf-8') as f:
        f.write(str(t))   
        f.write("\n")

if __name__ == "__main__":
    ulist = []
    findPash = "./terraria/terr_text.md"
    header={"user-agent":"Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.79 Safari/537.36"}
    url = "https://terraria.fandom.com/zh/wiki/Terraria_Wiki?variant=zh"
    html = getHtmlText(url,header)
    DownHtmlText(ulist,html,findPash)


#infocard.clearfix.compact.terraria.width-c.width-d.width-e