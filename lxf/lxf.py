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


def findHtmlText(html,text,findPash):
    soup = BeautifulSoup(html,"lxml")
    lis = soup.select("div.x-wiki-content.x-main-content p")
    for li in lis :
        if li.string != None:
            text.append(li.string)
            Downloadfild(li.string,findPash)
        HtmlImg = li.contents[0]
        if HtmlImg.name == "img" and HtmlImg != None :
            t = "![git-tutorial](https://www.liaoxuefeng.com" + HtmlImg["data-src"] +")"
            Downloadfild(t,findPash)

def Downloadfild(t,findPash):
    with open(findPash,"a",encoding='utf-8') as f:
        f.write(str(t))   
        f.write("\n")

def DownloadImg():
    pass
    #![git-tutorial](https://www.liaoxuefeng.com/files/attachments/918921150461184/0)

if __name__ == "__main__":
    ulist = {}
    text = []
    findPash = "./lxf/lxf_text.md"
    url = "https://www.liaoxuefeng.com/wiki/896043488029600"
    html = getHtmlText(url)
    findHtmlUrl(html,ulist)
    for TypeName,urll in ulist.items():
        htmll = getHtmlText(urll)
        Downloadfild("## "+TypeName,findPash)
        findHtmlText(htmll,text,findPash)
        #for t in text:
          #  Downloadfild(t,findPash)



