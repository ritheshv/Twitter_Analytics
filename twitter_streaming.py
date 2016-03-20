#Import the necessary methods from tweepy library
import json
import sys
from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream

#Variables that contains the user credentials to access Twitter API
access_token = "75317779-6vFx7gZtGz0veQKDNfTluSWomxYgsXhU3SNkPEgNx"
access_token_secret = "gBRewwhIxUw5PDo4lcaBXocWWrDSP7hrYtW44zjNLlI8d"
consumer_key = "xkBUhHFRaD7GXlAPRrZJmW5OB"
consumer_secret = "q3vD2wsviwtivgYs4fwrlNVFbWNv50bzvSrJ9b2W9zr7MX18qf"

#This is a basic listener that just prints received tweets to stdout.
class StdOutListener(StreamListener):

    def on_data(self, data):
        print data.encode('utf-8').strip()
#        line = json.loads(data)['text']
#        print line.encode('utf-8')
#        return True

    def on_error(self, status):
        print status


if __name__ == '__main__':

    #This handles Twitter authetification and the connection to Twitter Streaming API
    l = StdOutListener()
    auth = OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    stream = Stream(auth, l)

    #This line filter Twitter Streams to capture data by the keywords: 'python', 'javascript', 'ruby'
    stream.filter(track=['HP', 'Dell', 'Lenovo'])
