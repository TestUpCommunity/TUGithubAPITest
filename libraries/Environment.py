from github import Github

class Env:
    def __init__(self,token):
        self.github = Github(token=token)


