import praw

client_id = ""
client_secret= ""
user_agent=""
username=""
password=""

reddit= praw.Reddit(
    client_id=client_id,
    client_secret=client_secret,
    user_agent=user_agent,
    username=username,
    password=password

)
def get_memes():
    subredit = reddit.subreddit("memes")
    hot = subredit.hot(limit=10)
    url=[]
    for image in hot:
        url.append(image.url)
    return url

