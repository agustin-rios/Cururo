import inspect

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