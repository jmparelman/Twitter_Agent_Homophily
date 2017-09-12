import tweepy
import json

class Profiler():
    def __init__(self, authinfo):
        self.auth = tweepy.OAuthHandler(authinfo['key'],authinfo['secret'])


if __name__ == '__main__':
    authinfo = {'key':'GxkHPIVujBcAHNLZ3Na0f9x47',
                'secret':'sq1GLRd1cMqGKlqlFjSbYPsLYE8Ew4A5dqKdt3pwonAjXOicG6'}
    collecter = Profiler(authinfo)

