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


def _show_help():
    print('Usage: cururo [options]')
    print('Options:')
    print('  --item <item>           Add an item to the review.')
    print('  --openai-key <key>      OpenAI API key.')
    print('  --assistant-id <id>     OpenAI assistant ID.')
    print('  --action <action>       Custom action to perform on response.')
    print('  --publisher <publisher> Publisher to use for the review.')
    print('  -h, --help              Show this help message and exit.')


def _check_args(args):
    item_provided = args.item is not None
    openai_key_provided = args.openai_key is not None or DEFAULT_OPENAI_KEY is not None
    assistant_id_provided = args.assistant_id is not None or DEFAULT_ASSISTANT_ID is not None
    
    everything_provided = openai_key_provided and assistant_id_provided and item_provided

    if not everything_provided:
        print('Error: Missing required arguments.')
        _show_help()
        exit(1)

def main():
    parser = argparse.ArgumentParser(description='Review an item using OpenAI.')
    parser.add_argument('--item', type=str, help='Item to add to the review.')
    parser.add_argument('--openai-key', type=str, default=DEFAULT_OPENAI_KEY, help='OpenAI API key.')
    parser.add_argument('--assistant-id', type=str, default=DEFAULT_ASSISTANT_ID, help='OpenAI assistant ID.')
    parser.add_argument('--action', type=callable, default=DEFAULT_ACTION, help='Custom action to perform on response.')
    parser.add_argument('--publisher', type=Publisher, default=DEFAULT_PUBLISHER, help='Publisher to use for the review.')
    parser.add_argument('-h', '--help', action='store_true', help='Show this help message and exit.')
    
    args = parser.parse_args()
    _check_args(args)

    handler = ResponseHandler(publisher=args.publisher, additional_actions=[args.action])
    reviewer = Reviewer(openai_api_key=args.openai_key, assistant_id=args.assistant_id)
    # message = "Commit Message: Update README\n\nCommit Diff: Diff of README update"
    reviewer.append_item(args.item)
    reviewer.execute(handler.handle_response)
    # Define additional actions if needed

if __name__ == '__main__':
    main()
