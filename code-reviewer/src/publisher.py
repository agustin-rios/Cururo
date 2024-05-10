from .lib.github_pr import GithubPR 

class Publisher:
    def __init__(self, gh_api_key, _url):
        # self.gh = GithubPR(gh_api_key, _url)
        pass

    def publish(self, result):
        # Directly process and publish the result
        if result:  # Check if there is a result to publish
            print(f"Published result: {result}")