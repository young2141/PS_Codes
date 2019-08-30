# kakao_matching_point string parsing
# 80/100 point
import re
from pprint import pprint

class Data():
    def __init__(self):
        self.search = 0        
        self.point = 0
        self.calledby = []
        self.url = ''
        self.calls = set()
    

def solution(word, pages):
    word = word.lower()
    pages = [s.lower() for s in pages]    
    web_page = [Data() for _ in range( len(pages))]
    
    for web,page in zip(web_page,pages):        
        #body = re.search('<body>\\n(.*)',page)        
        #body = body.group(1)        
        regex = '[^a-z]('+word+')[^a-z]'        
        search = re.findall(regex,page)
        url = re.search('<meta .*content="(.+?)"/>',page)
        ext_links = re.findall('<a href="(.+?)">',page)
        #print(search,url.group(1),ext_links,body)
        web.search = len(search)
        web.url = url.group(1)
        web.calls = set(ext_links)
    
    for web in web_page:
        url = web.url        
        web.point += web.search
        for other in web_page:
            if other.url == url : continue
            if url in other.calls:
                web.calledby.append(other.url)
                web.point += other.search / len(other.calls)            
    
    answer,big = 0,0
    for i,web in enumerate(web_page):
        if  web.point > big:
            answer,big = i,web.point
    return answer    
   


if __name__ == "__main__":
    word,pages = 'Muzi', ["<html lang=\"ko\" xml:lang=\"ko\" xmlns=\"http://www.w3.org/1999/xhtml\">\n<head>\n  <meta charset=\"utf-8\">\n  <meta property=\"og:url\" content=\"https://careers.kakao.com/interview/list\"/>\n</head>  \n<body>\n<a href=\"https://programmers.co.kr/learn/courses/4673\"></a>#!MuziMuzi!)jayg07con&&\n\n</body>\n</html>", "<html lang=\"ko\" xml:lang=\"ko\" xmlns=\"http://www.w3.org/1999/xhtml\">\n<head>\n  <meta charset=\"utf-8\">\n  <meta property=\"og:url\" content=\"https://www.kakaocorp.com\"/>\n</head>  \n<body>\ncon%\tmuzI92apeach&2<a href=\"https://hashcode.co.kr/tos\"></a>\n\n\t^\n</body>\n</html>"]
    print(solution(word, pages))
