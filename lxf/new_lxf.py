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

# 获取子页面列表
def findHtmlUrl(html,ulist):
    soup = BeautifulSoup(html,"lxml")
    lis = soup.select("a.x-wiki-index-item")
    for TypeName in lis:
        ulist[TypeName.string] = "https://www.liaoxuefeng.com"+TypeName["href"]

# 对页面进行总处理
def findHtmlText(html,findPash):
    soup = BeautifulSoup(html,"lxml")
    lis = soup.select("div.x-wiki-content.x-main-content p")
    print(type(lis))
    #for li_1 in lis:
    for li in lis :
        #findImgP(li,findPash)
        if li.contents == None:
            Downloadfild(li.string,findPash)
        if li.contents != None:
            processTag(li,findPash)
        try:
            HtmlImg = li.contents[0]
        except:
            print("缺少图片",li.contents)    
        if HtmlImg.name == "img" :
            DownloadImg(HtmlImg,findPash)


# 对图片和p进行处理下载
def findImgP(li,findPash):
    if li.contents == None:
        Downloadfild(li.string,findPash)
    if li.contents != None:
        processTag(li,findPash)
    try:
        HtmlImg = li.contents[0]
    except:
        print("缺少图片",li.contents)    
    if HtmlImg.name == "img" :
        DownloadImg(HtmlImg,findPash)

# 对P的子节点进行处理下载
def processTag(li,findPash):
    for li_1 in li.contents:
        with open(findPash,"a",encoding='utf-8') as f:
            if str(li.string) != None:
                f.write(str(li_1.string))
    Downloadfild("",findPash)

# 基本下载
def Downloadfild(t,findPash):
    with open(findPash,"a",encoding='utf-8') as f:
        if str(t) != None:
            f.write(str(t))     
            f.write("\n\n")

# 图片下载
def DownloadImg(HtmlImg,findPash):
    t = "![git-tutorial](https://www.liaoxuefeng.com" + HtmlImg["data-src"] +")"
    with open(findPash,"a",encoding='utf-8') as f:
        if str(t) != None:
            f.write(str(t))   
            f.write("\n")
        else:
            print(".........")


if __name__ == "__main__":
    ulist = {}
    findPash = "./lxf/new_lxf_text.md"
    with open(findPash,"w") as f:
        f.write("")
    url = "https://www.liaoxuefeng.com/wiki/896043488029600"
    html = getHtmlText(url)
    findHtmlUrl(html,ulist)
    for TypeName,urll in ulist.items():
        htmll = getHtmlText(urll)
        Downloadfild("## "+TypeName,findPash)
        findHtmlText(htmll,findPash)
