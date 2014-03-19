from TwitterAPI import TwitterAPI


SEARCH_TERM = 'pizza'


CONSUMER_KEY = 'Hw7ON2F0LzfPi5GGCgFsA'
CONSUMER_SECRET = 'J9YESfbdQ6QnMg4lipoYHHu6pyh0QFUH6KaBxNE6n5c'
ACCESS_TOKEN_KEY = '36103735-k9zN6dHm9Axvkgr0ejNTPY2fL5aAVYtjVylXVUQIo'
ACCESS_TOKEN_SECRET = 'M8rJCJz6PMWqpm4KzJQfsEgkFa1qFYE6PPFIOm0NnLfDn'


api = TwitterAPI(CONSUMER_KEY, CONSUMER_SECRET, ACCESS_TOKEN_KEY, ACCESS_TOKEN_SECRET)

r = api.request('search/tweets', {'q':SEARCH_TERM})

for item in r:
	print(item['text'] if 'text' in item else item)
