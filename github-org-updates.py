#!/usr/bin/env python
from agithub import Github
import argparse
import datetime

parser = argparse.ArgumentParser()
parser.add_argument("orgname", type=str,
                    help="GitHub Organization name (github.com/orgname to use)")
args = parser.parse_args()

orgname = args.orgname

print "# Updates In The Past Week:\n"

github = Github()

now = datetime.datetime.utcnow()

for repo in github.orgs[orgname].repos.get(type='public')[1]:

    reponame = repo['name']
    updated = datetime.datetime.strptime(repo['pushed_at'], "%Y-%m-%dT%H:%M:%SZ")

    age = (now - updated).days + ((now - updated).seconds / (24*60*60.0))

    # Last week
    if age < 7.0:

        print "##", reponame, "\n"
        print "------------------------------------------------------------\n"
        print "<%s>\n" % repo['html_url']
        print "Open Issues: %d\n" % repo['open_issues_count']
        print "**Commits:**\n"

        print "<ul>"
        for commit in github.repos[orgname][reponame].commits.get()[1]:
            print "<li>%s</li>" % commit['commit']['message']
        print "</ul>"
        print "\n\n"

