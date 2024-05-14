class Publisher:
    def __init__(self, *args, **kwargs):
        pass

    def publish(self, response):
        if response is None:  # Check if there is a response to publish
            return
        # add your code here
        print(response)