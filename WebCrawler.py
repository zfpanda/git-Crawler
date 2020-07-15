# from urllib import request

import urllib.request
import re
import requests
#coding=utf-8
import time
import os



class WebCrawler():
    filepath = 'D:/WallPaper/'
    url = 'https://www.huya.com/g/4079'
    headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36'}
    
    root_pattern = '<li class="game-live-item"([\s\S]*?)</li>'
    imgurl_pattern = '<img class="pic" data-original="([\s\S]*?)" src'
    name_pattern = '<i class="nick" title="([\s\S]*?)">'

    

    def __get_content(self):

        result = urllib.request.Request(WebCrawler.url,headers=WebCrawler.headers)
        response = urllib.request.urlopen(result)
        htmls = response.read()

        htmls = str(htmls,encoding='utf-8')
        # print(htmls)
        a = 1
        return htmls

    def __cleaning(self,htmls):
        if not os.path.exists(WebCrawler.filepath):
            os.mkdir(WebCrawler.filepath)
        root_html = re.findall(WebCrawler.root_pattern,htmls)
        # print(root_html[0])
        for html in root_html:
            anchors = []
            imgurl = re.findall(WebCrawler.imgurl_pattern,html)
            img = imgurl[0].split('?')[0]
            name = re.findall(WebCrawler.name_pattern,html)[0]
            anchor = {'name':name,'imgurl':img}
            anchors.append(anchor)
            
            urllib.request.urlretrieve(img,'D:/WallPaper/'+name+'.jpg')
            # urllib.request.urlretrieve('https://anchorpost.msstatic.com/cdnimage/anchorpost/1033/65/c8c553b9e85c4dc8bfcf4e0ff1e0ce_4079_1590326305.jpg','D:/WallPaper/'+name+'.jpg')
            print('Download Finished '+ name)
            time.sleep(2)
        # print(anchors)
        a = 1


        
        
        a = 1

    def fetch(self):
        htmls = self.__get_content()
        self.__cleaning(htmls)

crawler = WebCrawler()
crawler.fetch()