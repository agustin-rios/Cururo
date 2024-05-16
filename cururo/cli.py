import argparse
import os
from .reviewer import Reviewer
from .util.publisher import Publisher
from .util.handler import ResponseHandler
from .lib.env_modes import EnvModes

def custom_action(response):
    pass # Custom action to perform on response

DEFAULT_OPENAI_KEY = os.getenv('OPENAI_KEY')
DEFAULT_ASSISTANT_ID = os.getenv('ASSISTANT_ID')
DEFAULT_MODE = 'production'
DEFAULT_ACTION = custom_action
DEFAULT_PUBLISHER = Publisher()


def main():
    parser = argparse.ArgumentParser(description='Review an item using OpenAI.')
    parser.add_argument('--item', type=str, required=True, help='Item to add to the review.')
    parser.add_argument('--openai-key', type=str, default=DEFAULT_OPENAI_KEY, help='OpenAI API key.', required=DEFAULT_OPENAI_KEY is None)
    parser.add_argument('--assistant-id', type=str, default=DEFAULT_ASSISTANT_ID, help='OpenAI assistant ID.', required=DEFAULT_ASSISTANT_ID is None)
    parser.add_argument('--mode', type=str, default=DEFAULT_MODE, help='Mode to run the review in.', choices=EnvModes.allowed_modes)
    parser.add_argument('--action', type=str, default=DEFAULT_ACTION, help='Custom action to perform on response.')
    parser.add_argument('--publisher', type=str, default=DEFAULT_PUBLISHER, help='Publisher to publish results.')
    # print version
    parser.add_argument('--version', action='version', version='%(prog)s 1.1.0')
    
    args = parser.parse_args()

    if isinstance(args.action, str):
        # Here you would dynamically import or determine the action function
        args.action = eval(args.action)  # Be careful with eval and consider security implications

    if isinstance(args.publisher, str):
        # Similar to action, instantiate your publisher or similarly handle it
        args.publisher = eval(args.publisher)  # Ensure security if using eval
        # print pubihser methods
        print(dir(args.publisher))


    handler = ResponseHandler(publisher=args.publisher, additional_actions=[args.action])
    reviewer = Reviewer(openai_api_key=args.openai_key, assistant_id=args.assistant_id, mode=args.mode)
    reviewer.append_item(args.item)
    reviewer.execute(handler.handle_response)

if __name__ == '__main__':
    main()
