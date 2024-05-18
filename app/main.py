import logging
import logstash
from collections import defaultdict

from flask import Flask, request

logger = logging.getLogger()
logger.setLevel(logging.INFO)
logger.addHandler(logstash.TCPLogstashHandler("logstash", 5044, version=1))

app = Flask("elkc-app")

posts = defaultdict(list)


@app.post("/post/<slug>")
def push_post(slug):
    data = request.json
    posts[slug].append(data)
    logging.info("new post", extra={"id": id(data)})
    return {"id": id(data)}


@app.get("/posts/describe")
def describe_posts():
    logging.info("describe", extra={"len": len(posts)})
    return list(posts.keys())
