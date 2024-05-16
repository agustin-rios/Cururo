from .lib.openai_assistant import OpenAIAssistant

class Reviewer:
    def __init__(self, openai_api_key, assistant_id, mode='production'):
        self.assistant = OpenAIAssistant(openai_api_key, assistant_id, mode=mode)
        self.steps = list()

    def add_item(self, item):
        response = self.assistant.add_and_retrieve_message(item, "user")
        if response and response != 'APIError: No response':
            return response
        return None

    def append_item(self, item=""):
        self.__append_step(self.add_item, item)

    def execute(self, callback):
        for step in self.steps:
            callback(step())

    def __append_step(self, func, *args, **kwargs):
        def wrapper(*args2, **kwargs2):
            # print(f"Running step: {func.__name__}")
            return func(*args, **kwargs)

        self.steps.append(wrapper)

