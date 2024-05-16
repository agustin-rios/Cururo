from ..util.publisher import Publisher
import requests

class WebPublisher(Publisher):
    def __init__(self, web_url, web_secret, processor=None, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.web_url = web_url
        self.web_secret = web_secret
        self.processor = processor

    def __create_post_response(self, response):
        """
        Post the response to the configured URL.
        """
        response = self.parse_response(response)

        if self.processor:
            response = self.processor(response)
            
        body = {'payload': response, 'secret': self.web_secret}
        requests.post(self.web_url, json=body)
