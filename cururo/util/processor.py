import json

class ResponseProcessor:
    def __init__(self, response_string):
        """
        Initialize with a JSON-formatted string response.
        """
        self.response = self.parse_response(response_string)

    @staticmethod
    def parse_response(response_string):
        """
        Parse the JSON string into a Python dictionary.
        """
        try:
            return json.loads(response_string)
        except json.JSONDecodeError:
            return {'message': response_string}



if __name__ == '__main__':
    # Usage
    response_string = '{"message": {"message": "Update function logic"}}'
    processor = ResponseProcessor(response_string)
    print(processor.response)
