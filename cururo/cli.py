import argparse
import os
from .reviewer import Reviewer
from .lib.web_publisher import WebPublisher
from .util.handler import ResponseHandler
from .lib.env_modes import EnvModes

def custom_action(response):
    print(f"CURURO_RESPONSE([C:START]{response}[C:END])")

DEFAULT_OPENAI_KEY = os.getenv('OPENAI_KEY')
DEFAULT_ASSISTANT_ID = os.getenv('ASSISTANT_ID')
DEFAULT_MODE = 'production'
DEFAULT_PUBLISHER = None


def main():
    parser = argparse.ArgumentParser(description='Review an item using OpenAI.')
    parser.add_argument('--item', type=str, required=True, help='Item to add to the review.')
    parser.add_argument('--openai-key', type=str, default=DEFAULT_OPENAI_KEY, help='OpenAI API key.', required=DEFAULT_OPENAI_KEY is None)
    parser.add_argument('--assistant-id', type=str, default=DEFAULT_ASSISTANT_ID, help='OpenAI assistant ID.', required=DEFAULT_ASSISTANT_ID is None)
    parser.add_argument('--mode', type=str, default=DEFAULT_MODE, help='Mode to run the review in.', choices=EnvModes.allowed_modes)
    parser.add_argument('--web-url', type=str, help='URL to post the response to.', default=None)
    parser.add_argument('--web-secret', type=str, help='Secret to use when posting the response to the URL.', default=None)
    parser.add_argument('--web-processor', type=str, help='Processor to use when posting the response to the URL.', default=None)
    parser.add_argument('--version', action='version', version='%(prog)s 1.1.1')
    
    args = parser.parse_args()

    if args.web_url and not args.web_secret:
        parser.error('--web-secret is required when using --web-url')

    if args.web_processor:
        try:
            processor = eval(args.web_processor)
        except:
            parser.error('--web-processor must be a valid callable')
        args.web_processor = processor

    # check url
    if args.web_url:
        publisher = WebPublisher(web_url=args.web_url, web_secret=args.web_secret, processor=args.web_processor)
    else:
        publisher = DEFAULT_PUBLISHER

    handler = ResponseHandler(publisher=publisher, additional_actions=[args.action])
    reviewer = Reviewer(openai_api_key=args.openai_key, assistant_id=args.assistant_id, mode=args.mode)
    reviewer.append_item(args.item)
    reviewer.execute(handler.handle_response)

if __name__ == '__main__':
    main()
