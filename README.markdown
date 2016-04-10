# GitHub Org Updates

![Code Language](https://img.shields.io/badge/language-python-green.svg)

Use the GitHub API to create blog-like, "what we've been up to" posts for a GitHub Organization using a composite of Issue and milestone statuses and individual commit logs/messages.


## Install

    $ pip install -r requirements.txt


## Run

    $ ./github-org-updates.py orgname > new_updates.md

Will gather all the commits and issues over last calendar week and print a blog post to `stdout`.

See the output of 

    $ ./github-org-updates.py --help

for more configuration options.
