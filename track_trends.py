from __future__ import print_function
from twitter.stream import TwitterStream, Timeout, HeartbeatTimeout, Hangup
from twitter.oauth import OAuth
from twitter.util import printNicely
from datetime import datetime
import psycopg2

class DB:
    def __init__(self, connection_string, driver):
        self.connection = driver.connect(connection_string)
        self.cursor = self.connection.cursor()

        

def main():
    try:
        # TODO: from config
        conn_string = "host='localhost' dbname='trends' user='trends_user' password='password'"
        db = DB(conn_string, psycopg2)

        track_keywords = keywords_to_track(db)
        stream_iterator = get_stream_iterator(track_keywords)
        collect_trends(stream_iterator, increment_trend_scores, db)
    except StandardError as err:
        print(err)
    finally:
        db.cursor.close()
        db.connection.close()

def keywords_to_track(db):
    db.cursor.execute("SELECT name FROM trends_keyword WHERE is_active = true")
    rows = db.cursor.fetchall()
    return ",".join(map(lambda k: k[0], rows))
    
def get_stream_iterator(track_keywords):
    # TODO: from config
    args = {
        'token': "1010873339819196416-3yDJVTlPLOyptBjx8DAeB9feAXSpJp",
        'token_secret': "i2ddWam867Y1wWYxvC0b4KcYViZuQ36hDoHkYNm8CCUko",
        'consumer_key': "Y3eSkzd8OPea2lUoXypISoBT2",
        'consumer_secret': "nZOjyOuzBjgUgEzygK4zU3T6PiI4MnTLdHSm1Y2JuHiVW00Hfv",
        'timeout': 8000,
        'heartbeat_timeout': 3000,
        'track_keywords': track_keywords,
        'no_block': True
    }

    auth = OAuth(args['token'], args['token_secret'], args['consumer_key'], args['consumer_secret'])

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
    
    return tweet_iter

def collect_trends(iterator, collect_function, db):
    for tweet in iterator:
        if tweet is None:
            printNicely("-- None --")
        elif tweet is Timeout:
            printNicely("-- Timeout --")
        elif tweet is HeartbeatTimeout:
            printNicely("-- Heartbeat Timeout --")
        elif tweet is Hangup:
            printNicely("-- Hangup --")
        elif tweet.get('entities', {}).get('hashtags'):
            collect_function(db, map(lambda h: h['text'], tweet['entities']['hashtags']))

# TODO: optimize
def increment_trend_scores(db, trends = []):
    update_sql = "UPDATE trends_trend SET score = score+1, last_spotted_at=%s WHERE name = %s"
    insert_sql = "INSERT INTO trends_trend (name, score, last_spotted_at) VALUES(%s, 1, %s)"

    try:
        for trend in trends:
            db.cursor.execute(update_sql, (datetime.now(), trend,))
            if db.cursor.rowcount == 0:
                db.cursor.execute(insert_sql, (trend, datetime.now(),))

        db.connection.commit()
    except StandardError as err:
            print(err)

if __name__ == '__main__':
    main()