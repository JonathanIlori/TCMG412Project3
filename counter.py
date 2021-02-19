import os
import urllib.request

FilePath = './http_access_log.txt'
FileExists = os.path.exists(FilePath)

if FileExists == False:
    print("It doesn't appear you have the data, downloading it now")
    url = "https://s3.amazonaws.com/tcmg476/http_access_log"
    urllib.request.urlretrieve(url,"./http_access_log.txt")

else:
    print ("It looks like you already have the file")

print ("Reviewing the data now")
TextFile = open("http_access_log.txt")
Log = TextFile.read()
LastYearCount = Log.count("1995")
FirstYearCount = Log.count("1994")
print("Number of accsesses from 1995:", LastYearCount)
print("Number of accsesses from 1994 and 1995:", FirstYearCount + LastYearCount)
