from __future__ import absolute_import, print_function

import tweepy

#OAuth Authentication
consumer_key='rwyt0EdSlwqFVMHflajKAvIlS'
consumer_secret='RkeG12RkiIHTLOC3oERUvRtTayyaZGIKX8I2FL23RFNgDJkGjY'

access_token='4621786103-QaE3WrRdyLyO05WxASCVwP2hf63ioOLf9YgQKBR'
access_token_secret='O9uPax6pfpQ5vnJOqQT0BYrrq3oBwDt6X4jT09cT4EpRt'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.secure = True
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

#Print user profile
print('PROFILE')
print('User ID: ' + api.me().id_str)
print('Screen Name: ' + api.me().screen_name)
print('User name: ' + api.me().name)
print('User Description: ' + api.me().description)
print('The Number of Followers: ' + str(api.me().followers_count))
print('The Number of Friends: ' + str(api.me().friends_count))
print('The Number of Statuses: ' + str(api.me().statuses_count))
print('User URL: ' + api.me().url)

#Print user timeline
print('\nTIMELINE')
for status in tweepy.Cursor(api.user_timeline).items(5):
    print('Tweet: ' + status.text) 

#Print user followers
print('\nFOLLOWERS')
for follower in tweepy.Cursor(api.followers).items(5):
    print(follower.screen_name)

#print user friends
print('\nFRIENDS')
for friend in tweepy.Cursor(api.friends).items(5):
    print(friend.screen_name) 




