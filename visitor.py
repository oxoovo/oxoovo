from github import Github
import os

repo = Github(os.environ['GITHUB_TOKEN']).get_repo(os.environ['GITHUB_REPOSITORY'])
issue = repo.get_issue(number=int(os.environ['ISSUE_NUMBER']))
issue_author = '* ' + issue.user.login

a = open("README.md", "a")
a.write(issue_author)
a.close()
