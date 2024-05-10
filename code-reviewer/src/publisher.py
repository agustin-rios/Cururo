import json
from .lib.github_pr import GithubPR
from .processor import CodeReviewProcessor


class Publisher:
    def __init__(self, gh_api_key, _url):
        # self.gh = GithubPR(gh_api_key, _url)
        pass

    def publish(self, response):
        if response is None:  # Check if there is a response to publish
            return
        processor = CodeReviewProcessor(response)
        full_report = processor.create_full_report()
        print(full_report)