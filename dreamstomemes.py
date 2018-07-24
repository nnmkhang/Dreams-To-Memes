import os.path
import praw
import urllib
print("\n")

#username: memestodreams1   
#password: 123456
#client id: MbP-ITqzQxx-SA
#secret: rNhq65-IYUnIVlfdiBTNfhOdiJ8

def downloadURL(url): # function downloads the url specified to a folder
    picUrl = url
    picName = url.split("/")[-1]
    

    if(picName.split(".")[-1] == "jpg" or picName.split(".")[-1] == "png"):
        
        picName = directory+picName
        #print picName
        urllib.urlretrieve(picUrl, picName)
    else:
        picUrl = ("https://i.imgur.com/" + picName +".jpg")
        picName = (directory+picName+".jpg")
        #print picUrl 
        urllib.urlretrieve(picUrl, picName)

print("test")
directory = input("Where to download?")




reddit = praw.Reddit(client_id = "MbP-ITqzQxx-SA",
                     client_secret = "rNhq65-IYUnIVlfdiBTNfhOdiJ8",
                     username = "memestodreams1",
                     password = "123466",
                     user_agent = "memestodreamsscript" )
                    