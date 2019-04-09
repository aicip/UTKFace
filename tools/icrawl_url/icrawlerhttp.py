import re
import urllib
import urllib2
import os

def getHtml(url):
    page = urllib.urlopen(url)
    html = page.read()
    return html

def mkdir(path):
    path = path.strip()

    isExists = os.path.exists(path)
    if not isExists:
        print u'creating new name',path,u'folder'
        os.makedirs(path)
        return True
    else:
        print u'named',path,u'building finish'
        return False

def saveImages(imglist,name):
    number = 1
    for imageURL in imglist:
        splitPath = imageURL.split('.')
        fTail = splitPath.pop()
        if len(fTail) > 3:
            fTail = 'jpg'
        fileName = name + "/" + str(number) + "." + fTail
     
        try:
            u = urllib2.urlopen("http://www.azpbs.org/spellingbee/2012/"+imageURL)
            data = u.read()
            f = open(fileName,'wb+')
            f.write(data)
            print u'saving image as',fileName
            f.close()
        except urllib2.URLError as e:
            print (e.reason)
        number += 1



def getAllImg(html):

    reg = r'src="(.+?\.jpg)"'
    imgre = re.compile(reg)
    imglist = imgre.findall(html)
    print imglist
    return imglist



if __name__ == '__main__':
    html = getHtml("http://www.azpbs.org/spellingbee/2012/")
    path = u'image'
    mkdir(path)
    imglist = getAllImg(html)
    saveImages(imglist,path)