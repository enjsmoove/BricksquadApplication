import tweepy

ckey='Hw7ON2F0LzfPi5GGCgFsA'
csecret='J9YESfbdQ6QnMg4lipoYHHu6pyh0QFUH6KaBxNE6n5c'
atoken='36103735-k9zN6dHm9Axvkgr0ejNTPY2fL5aAVYtjVylXVUQIo'
asecret='M8rJCJz6PMWqpm4KzJQfsEgkFa1qFYE6PPFIOm0NnLfDn'

public_tweets = tweepy.API.get_status('436252998327877600')
for tweet in public_tweets:
    print tweet.text
