from matplotlib.pyplot import text
import slack
import os

from pathlib import Path
from dotenv import load_dotenv


env_path = Path(".") / ".env"
load_dotenv(dotenv_path=env_path)

client = slack.WebClient(token=os.environ["SLACK_TOKEN"])

#Channel Creation Logic - Based on Subject and Authorized User List
name = "bot-test-1"
users = os.environ["USERS"]

resp = client.conversations_list()
channels = {d["name"]: d["id"] for d in resp["channels"]}

if name not in list(channels.keys()):
    response = client.conversations_create(name=name, is_private=False)
    channel_id = response["channel"]["id"]
else:
    channel_id = channels[name]

channel_name = "#" + name

client.conversations_invite(channel=channel_id, users=users)

# Message Logic - Crawl and post filtered texts
client.chat_postMessage(channel=channel_name, text="Hello Houston this is a test.")