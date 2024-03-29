from github import Github
import os

repo = Github(os.environ['GITHUB_TOKEN']).get_repo(os.environ['GITHUB_REPOSITORY'])
issue = repo.get_issue(number=int(os.environ['ISSUE_NUMBER']))
issue_author2 = issue.user.login
issue_author = '@' + issue.user.login
repo_owner = '@' + os.environ['REPOSITORY_OWNER']
issue.create_comment("Thank you for adding your name, " + issue_author2 + " 😀")
issue.edit(state="closed")

with open("README.md", "r") as f:
    content = f.read()
  
with open("README.md", "w") as f:
    f.write(content + "\n* " + issue_author2)
