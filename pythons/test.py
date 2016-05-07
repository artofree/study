import os, urllib.request, urllib.error, urllib.parse, threading, codecs, time

theUrl = r'http://test.alltobid.com/'
thePage = urllib.request.urlopen(theUrl).read()
with codecs.open("/Users/guo/Downloads/1", 'wb') as f:
    f.write(thePage)
i =0
