import praw

reddit = praw.Reddit(
    client_id="aHk3G-s2_eXOLTO_7Yptfw",
    client_secret="o9gZYqkVcbV6G_EDzJeAJ_o7OuaXzg",
    password="888555662Jc",
    user_agent="chao",
    username="Historical-Shock-882",
)

# Create a submission to r/test
reddit.subreddit("test").submit("Test Submission", url="https://reddit.com")

# Comment on a known submission
#submission = reddit.submission(url="https://www.reddit.com/comments/5e1az9")
submission = reddit.submission(url="https://www.reddit.com/r/UKJobs/comments/1bboni9/why_are_uk_salaries_so_low/")
submission.reply("Super rad!")

# Reply to the first comment of a weekly top thread of a moderated community
submission = next(reddit.subreddit("politics").top(time_filter="week"))
submission.comments[0].reply("An automated reply")

# Output score for the first 256 items on the frontpage
for submission in reddit.front.hot(limit=256):
    print(submission.score)

# Obtain the moderator listing for r/test
for moderator in reddit.subreddit("test").moderator():
    print(moderator)