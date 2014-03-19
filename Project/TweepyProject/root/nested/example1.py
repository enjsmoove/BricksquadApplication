from tweepy import Stream
from tweepy import OAuthHandler
from tweepy.streaming import StreamListener
import time
 

ckey='Hw7ON2F0LzfPi5GGCgFsA'
csecret='J9YESfbdQ6QnMg4lipoYHHu6pyh0QFUH6KaBxNE6n5c'
atoken='36103735-k9zN6dHm9Axvkgr0ejNTPY2fL5aAVYtjVylXVUQIo'
asecret='M8rJCJz6PMWqpm4KzJQfsEgkFa1qFYE6PPFIOm0NnLfDn'

class listener(StreamListener):
    
        def on_data(self,data):
            try:
                
                print data
                saveFile = open('twitDB.csv','a')
                saveFile.write(data)
                saveFile.write('\n')
                saveFile.close()
           
                return True
            except BaseException, e:
                print 'failed ondata,',str(e)
                time.sleep(5)
        def on_error(self,status):
            print status
            
auth = OAuthHandler(ckey,csecret)
auth.set_access_token(atoken,asecret)
twitterStream =Stream(auth, listener())
twitterStream.filter(track=["Obama"])