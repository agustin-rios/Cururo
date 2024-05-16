import inspect
import json

class Publisher:
    def __init__(self, *args, **kwargs):
        pass

    def publish(self, response):
        if response is None:  # Check if there is a response to publish
            return
        
        # Dynamically find and run all methods starting with __create_
        methods = inspect.getmembers(self, predicate=inspect.ismethod)
        for name, method in methods:
            mangled_name = f"_{self.__class__.__name__}__create_"
            if name.startswith(mangled_name):
                method(response)

    @staticmethod
    def parse_response(response_string):
        """
        Parse the JSON string into a Python dictionary.
        """
        try:
            return json.loads(response_string)
        except json.JSONDecodeError:
            return response_string
