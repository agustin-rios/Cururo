import argparse
import os
from .reviewer import Reviewer
from .util.publisher import Publisher
from .util.handler import ResponseHandler

def custom_action(response):
    pass # Custom action to perform on response

DEFAULT_OPENAI_KEY = os.getenv('OPENAI_KEY')
DEFAULT_ASSISTANT_ID = os.getenv('ASSISTANT_ID')
DEFAULT_ACTION = custom_action
DEFAULT_PUBLISHER = Publisher()


def main():
    parser = argparse.ArgumentParser(description='Review an item using OpenAI.')
    parser.add_argument('--item', type=str, required=True, help='Item to add to the review.')
    parser.add_argument('--openai-key', type=str, default=DEFAULT_OPENAI_KEY, help='OpenAI API key.', required=DEFAULT_OPENAI_KEY is None)
    parser.add_argument('--assistant-id', type=str, default=DEFAULT_ASSISTANT_ID, help='OpenAI assistant ID.', required=DEFAULT_ASSISTANT_ID is None)
    parser.add_argument('--action', type=callable, default=DEFAULT_ACTION, help='Custom action to perform on response.')
    parser.add_argument('--publisher', type=Publisher, default=DEFAULT_PUBLISHER, help='Publisher to use for the review.')
    
    args = parser.parse_args()

    if isinstance(args.action, str):
        # Here you would dynamically import or determine the action function
        args.action = eval(args.action)  # Be careful with eval and consider security implications

    if isinstance(args.publisher, str):
        # Similar to action, instantiate your publisher or similarly handle it
        args.publisher = eval(args.publisher)  # Ensure security if using eval


    handler = ResponseHandler(publisher=args.publisher, additional_actions=[args.action])
    reviewer = Reviewer(openai_api_key=args.openai_key, assistant_id=args.assistant_id)
    reviewer.append_item(args.item)
    reviewer.execute(handler.handle_response)

if __name__ == '__main__':
    main()
