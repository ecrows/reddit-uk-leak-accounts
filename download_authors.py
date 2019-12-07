#!/usr/bin/env python
# coding: utf-8

from psaw import PushshiftAPI
import json

api = PushshiftAPI()

# Load list of users.
# The list of users associated with this campaign is based one the official release from Reddit at:
# https://www.reddit.com/r/redditsecurity/comments/e74nml/suspected_campaign_from_russia_on_reddit/
authors = []

with open("./data/userlist.csv") as f:
    authors = f.read().splitlines()

# Perform searches using Pushshift API
contributions_by_author = []

for author in authors:
    entry = {}
    entry["author"] = author
    
    submissions = api.search_submissions(limit=99999, author=author)
    entry["submissions"] = list(submissions)
    
    comments = api.search_comments(limit=99999, author=author)
    entry["comments"] = list(comments)
    
    contributions_by_author.append(entry)

# Drop everything but the dictionary keys
refined_results = []

for contr in contributions_by_author:
    entry = {}
    entry["author"] = contr["author"]
    entry["submissions"] = []
    entry["comments"] = []
    
    for s in contr["submissions"]:
        entry["submissions"].append(s.d_)
        
    for c in contr["comments"]:
        entry["comments"].append(c.d_)
    
    refined_results.append(entry)

# Write the results to a file
with open("./data/author_activity.json", "w") as out:
    json.dump(refined_results, out)
    