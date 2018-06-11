#encoding=utf-8
"刷新浪博客等级软件"
import urllib,urllib2,cookielib,re,threading,requests,time
def sina_blog(url):
    aid=re.findall("blog_(.*?)\.html",url)[0]
    cookie=cookielib.CookieJar()
    opener=urllib2.build_opener(urllib2.HTTPCookieProcessor(cookie))
    opener.addheaders=[
        ("Host","comet.blog.sina.com.cn"),("User-Agent","Mozilla/5.0 (Windows NT 6.3; WOW64; rv:40.0) Gecko/20100101 Firefox/40.0"),("Referer",url)
    ]
    urllib2.install_opener(opener)
    html=urllib2.urlopen("http://comet.blog.sina.com.cn/api?maintype=hits&act=4&aid=%s"%aid).read()
    print html

if __name__=="__main__":

    for x in range(500):
        if x%200==0:
            time.sleep(2)
            # sina_blog("http://blog.sina.com.cn/s/blog_17e5514330102xc4i.html")#在这里输入任意一个新浪博客文章页面URL即可
            url="http://blog.sina.com.cn/s/blog_143734b7e0102xeqx.html"
            x=threading.Thread(target=sina_blog,args=(url,))
            x.start()
        else:
            url="http://blog.sina.com.cn/s/blog_143734b7e0102xeqx.html"
            x=threading.Thread(target=sina_blog,args=(url,))
            x.start()

