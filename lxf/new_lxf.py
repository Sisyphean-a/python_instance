from bs4 import BeautifulSoup
import requests
import bs4
import os

def getHtmlText(url):
    header={"user-agent":"Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.79 Safari/537.36"}
    r = requests.get(url,headers=header,timeout=30)
    r.encoding = r.apparent_encoding
    a = r.text
    return a 

def findHtmlUrl(html,ulist):
    soup = BeautifulSoup(html,"lxml")
    lis = soup.select("a.x-wiki-index-item")
    for TypeName in lis:
        ulist[TypeName.string] = "https://www.liaoxuefeng.com"+TypeName["href"]


def findHtmlText(html,findPash):
    soup = BeautifulSoup(html,"lxml")
    lis = soup.select("div.x-wiki-content.x-main-content")
    for li in lis :
        if li.string != None:
            Downloadfild(li.string,findPash)
        try:
            HtmlImg = li.contents[0]
        except:
            print("缺少图片",li.contents)    
        if HtmlImg.name == "img" :
            DownloadImg(HtmlImg,findPash)

def Downloadfild(t,findPash):
    with open(findPash,"a",encoding='utf-8') as f:
        f.write(str(t))   
        f.write("\n")

def DownloadImg(HtmlImg,findPash):
    t = "![git-tutorial](https://www.liaoxuefeng.com" + HtmlImg["data-src"] +")"
    with open(findPash,"a",encoding='utf-8') as f:
        f.write(str(t))   
        f.write("\n")

if __name__ == "__main__":
    ulist = {}
    findPash = "./lxf/new_lxf_text.md"
    url = "https://www.liaoxuefeng.com/wiki/896043488029600"
    html = getHtmlText(url)
    findHtmlUrl(html,ulist)
    for TypeName,urll in ulist.items():
        htmll = getHtmlText(urll)
        Downloadfild("## "+TypeName,findPash)
        findHtmlText(htmll,findPash)
        #for t in text:
          #  Downloadfild(t,findPash)