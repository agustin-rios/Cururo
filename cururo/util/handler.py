class ResponseHandler:
    def __init__(self, publisher=None, logger=None, additional_actions=None):
        """
        Initializes the response handler with optional publisher, logger, and additional actions.

        Args:
        publisher (Publisher): An instance of Publisher class for publishing results.
        logger (Logger): A logging instance to log responses.
        additional_actions (list of callable): Additional actions to be executed with the response.
        """
        self.publisher = publisher
        self.logger = logger
        self.additional_actions = additional_actions if additional_actions else []

    def handle_response(self, response):
        """
        Handles the response using configured methods.

        Args:
        response (str): The response to handle.
        """
        if self.publisher and response:
            self.publisher.publish(response)

        if self.logger:
            self.logger.log(response)

        for action in self.additional_actions:
            action(response)
