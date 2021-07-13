"""Scrapes Twitter using Twint and returns a JSON response via FastAPI"""

import twint

from fastapi import FastAPI

app = FastAPI()


@app.get("/user/{user_id}")
def get_tweets(user_id: str):
    """Takes a username and returns a list of their last 100 tweets"""
    tweets = []
    config = twint.Config()
    config.Username = user_id
    config.Limit = 100
    config.Store_object = True
    config.Store_object_tweets_list = tweets
    config.Hide_output = True
    twint.run.Search(config)
    return tweets
