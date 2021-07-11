import twint

from fastapi import FastAPI

app = FastAPI()


@app.get("/user/{user_id}")
def get_tweets(user_id: str):
    tweets = []
    c = twint.Config()
    c.Username = user_id
    c.Limit = 20
    c.Store_object = True
    c.Store_object_tweets_list = tweets
    c.Hide_output = True
    twint.run.Search(c)
    return tweets
