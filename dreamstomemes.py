import os.path
import praw
import urllib.request
import random
from PIL import Image
from pytesseract import *
import re

#username: memestodreams1   
#password: 123456
#client id: xbN4kVxAil3Sng
#secret: rNhq65-IYUnIVlfdiBTNfhOdiJ8

def dreamstomemes():
#"C:\\Users\\nnmkh\\Desktop\\memes\\"
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


    # gets a random number between 1 and 100 
    rand = random.randint(1,100)

    #/home/pi/Desktop/Dreams-To-Memes/
    # this one is set to inside the project folder
    print("test")
    directory = "C:\\Code\\Python\\Dreams-To-Memes\\static\\img\\"
    print(directory)



    reddit = praw.Reddit(client_id = "xbN4kVxAil3Sng",
                        client_secret = "wkRHF4kpJllOg2-HdjXwQyNyOtw",
                        username = "memestodreams1",
                        password = "123456",
                        user_agent = "memestodreamsscript" )

    sub = list(reddit.subreddit('greentext').top(time_filter= "all", limit =100))[rand] 
    

    print(sub.title)
    print(sub.url)
    filename = (directory+"meme"+".jpg")
    print(filename)
    urllib.request.urlretrieve(sub.url,filename)

    im = Image.open(filename)
    text = image_to_string(im, lang= "eng")
    #print(text) 
    text = text.replace("1","I")
    text = text.replace("|","I")
    print(text)
    return(sub.url)
    # need to go thru the text and make it look better 


        #https://www.reddit.com/r/redditdev/comments/5k9zui/how_to_get_nth_most_upvoted_post_in_a_subreddit/?st=jk0fj5vi&sh=775b4848
        #got downloading working, now gotta get random images, use rand num gen, and 
        # then just get that post num.
        # after use the OCR To transfer to string and write it to a file 
