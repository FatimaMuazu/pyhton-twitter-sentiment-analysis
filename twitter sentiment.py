from tweepy import Stream
from tweepy import OAuthHandler
from tweepy.streaming import StreamListener
#import time
from textblob import TextBlob
import json

ckey = 'LUaL5bgH3YUeJj2XOg3NEx1BS'
csecret= 'Fsa4TlW2sR4CYRW3ncUWmgNNEFOpTLa7xcgnBC2UUheywvv7X8'
atoken = '437431356-IRU8AM8rntoVG1g5xzCXXlnUcw8NaJWJBiMpZPEh'
asecret = 'VHGsqzgb4679h5ivEYZlIiUmG0h1nc9nfEUPEF3tiuPmL'



#defining listener class
class listener (StreamListener):
    
    def on_data(self, data):
       #if self.listener.on_data(data) is false:
        #   self.running=False
        
       all_data=json.loads(data)

       tweet = TextBlob(all_data["text"])
       print (tweet)
       print (tweet.sentiment.polarity)
       
       
       if tweet.sentiment.polarity<0:
           sentiment="negative"
       elif tweet.sentiment.polarity==0:
           sentiment="neutral"
       else:
           sentiment="positive"

       print (sentiment)
       print (tweet.sentiment.subjectivity)
       output = open('tweets-in.csv','a')
       output.write(sentiment)
       output.write('\n')
       output.close()
       return True
       
        
    #def on_status(self, status):
    #   print(status.text)


    #def on_error(self, status_code):
    #   if status_code==420:
    #        return False
    def on_error(self, status):
      print (status)
      return True
auth=OAuthHandler(ckey, csecret)
auth.set_access_token(atoken, asecret)
twitterStream = Stream(auth,listener())
twitterStream.filter(track=["#trump"])

#SAVING TO A CSV FILE
