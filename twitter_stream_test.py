"""
Example program for the Stream API. This prints public status messages
from the "sample" stream as fast as possible. Use -h for help.
"""

from __future__ import print_function

# import argparse

from twitter.stream import TwitterStream, Timeout, HeartbeatTimeout, Hangup
from twitter.oauth import OAuth
from twitter.util import printNicely

def main():
    keywords = "russia,trump"

    args = {
        'token': "1010873339819196416-3yDJVTlPLOyptBjx8DAeB9feAXSpJp",
        'token_secret': "i2ddWam867Y1wWYxvC0b4KcYViZuQ36hDoHkYNm8CCUko",
        'consumer_key': "Y3eSkzd8OPea2lUoXypISoBT2",
        'consumer_secret': "nZOjyOuzBjgUgEzygK4zU3T6PiI4MnTLdHSm1Y2JuHiVW00Hfv",
        'timeout': 8000,
        'heartbeat_timeout': 3000,
        'track_keywords': keywords,
        'no_block': True
    }

    # When using twitter stream you must authorize.
    auth = OAuth(args['token'], args['token_secret'], args['consumer_key'], args['consumer_secret'])

    # These arguments are optional:
    stream_args = dict(
        timeout = args['timeout'],
        block = not args['no_block'],
        heartbeat_timeout = args['heartbeat_timeout'])

    query_args = dict()
    if args.get('track_keywords'):
        query_args['track'] = args['track_keywords']

    stream = TwitterStream(auth=auth, **stream_args)
    if args.get('track_keywords'):
        tweet_iter = stream.statuses.filter(**query_args)
    else:
        tweet_iter = stream.statuses.sample()

    # Iterate over the sample stream.
    for tweet in tweet_iter:
        # You must test that your tweet has text. It might be a delete
        # or data message.
        if tweet is None:
            printNicely("-- None --")
        elif tweet is Timeout:
            printNicely("-- Timeout --")
        elif tweet is HeartbeatTimeout:
            printNicely("-- Heartbeat Timeout --")
        elif tweet is Hangup:
            printNicely("-- Hangup --")
        elif tweet.get('entities', {}).get('hashtags'):
            print(map(lambda h: h['text'], tweet['entities']['hashtags']))
        # else:
            # printNicely("-- Some data: " + str(tweet))

if __name__ == '__main__':
    main()