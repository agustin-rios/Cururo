import argparse
import os
from .reviewer import Reviewer
from .util.handler import ResponseHandler

DEFAULT_OPENAI_KEY = os.getenv('OPENAI_KEY')
DEFAULT_ASSISTANT_ID = os.getenv('ASSISTANT_ID')
DEFAULT_GH_API_KEY = os.getenv('GH_API_KEY')
DEFAULT_PR_URL = os.getenv('PR_URL')

def _show_help():
    print('Usage: cururo [options]')
    print('Options:')
    print('  --openai-key <key>      OpenAI API key.')
    print('  --assistant-id <id>     OpenAI assistant ID.')
    print('  --gh-api-key <key>      GitHub API key.')
    print('  --pull-request-url <url> GitHub pull request URL.')
    print('  -h, --help              Show this help message and exit.')

def _check_args(args):
    openai_key_provided = args.openai_key is not None or DEFAULT_OPENAI_KEY is not None
    assistant_id_provided = args.assistant_id is not None or DEFAULT_ASSISTANT_ID is not None
    gh_api_key_provided = args.gh_api_key is not None or DEFAULT_GH_API_KEY is not None
    pr_url_provided = args.pull_request_url is not None or DEFAULT_PR_URL is not None

    everything_provided = openai_key_provided and assistant_id_provided and gh_api_key_provided and pr_url_provided

    if not everything_provided:
        print('Error: Missing required arguments.')
        _show_help()
        exit(1)

def main():
    parser = argparse.ArgumentParser(description='Review a GitHub pull request.')
    parser.add_argument('--openai-key', type=str, default=DEFAULT_OPENAI_KEY, help='OpenAI API key.')
    parser.add_argument('--assistant-id', type=str, default=DEFAULT_ASSISTANT_ID, help='OpenAI assistant ID.')
    parser.add_argument('--gh-api-key', type=str, default=DEFAULT_GH_API_KEY, help='GitHub API key.')
    parser.add_argument('--pull-request-url', type=str, default=DEFAULT_PR_URL, help='GitHub pull request URL.')
    
    args = parser.parse_args()
    _check_args(args)

    publisher = Publisher(gh_api_key=args.gh_api_key, _url=args.pull_request_url)
    reviewer = Reviewer(openai_api_key=args.openai_key, assistant_id=args.assistant_id)
    reviewer.append_commit("Update README", "Diff of README update")
    # Define additional actions if needed
    def custom_action(response):
        print(f"Custom action for response: {response}")

    handler = ResponseHandler(publisher=publisher, additional_actions=[custom_action])
    reviewer.execute(handler.handle_response)

if __name__ == '__main__':
    main()
