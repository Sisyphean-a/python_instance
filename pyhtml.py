from bs4 import BeautifulSoup
import requests

def getHtmlText(url,header):
    r = requests.get(url,headers=header,timeout=30)
    r.encoding = r.apparent_encoding
    a = r.text
    return a 

def DownHtmlText(ulist,html,findPash):
    soup = BeautifulSoup(html,"lxml")
    lis = soup.select("tbody#separatorline")
    print("1 1")
    #print(len(lis))
    #print(lis)

if __name__ == "__main__":
    ulist = []
    findPash = "./terraria/terr_text2.md"
    header={"user-agent":"Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.79 Safari/537.36"}
    url = "https://www.52pojie.cn/forum-16-1.html"
    html = getHtmlText(url,header)
    DownHtmlText(ulist,html,findPash)