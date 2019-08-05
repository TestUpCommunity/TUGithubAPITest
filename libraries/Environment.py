from github import Github

class Env:
    def __init__(self,api_root_url,token):
        self.github = Github(api_root_url,token=token)


