import praw
client_id = "9q948ijW8JsuSA"
client_secret= "tNBHKMsGiVLE3DRYnec5rxkDYMWrmg"
user_agent="scrape_meme"
username="Throwawayforpraw33"
password="Rv-<.2R35mZRgd-"

reddit= praw.Reddit(
    client_id=client_id,
    client_secret=client_secret,
    user_agent=user_agent,
    username=username,
    password=password

)
subredit = reddit.subreddit("memes")
hot = subredit.hot(limit=10)
url=[]
for image in hot:
    url.append(image.url)


