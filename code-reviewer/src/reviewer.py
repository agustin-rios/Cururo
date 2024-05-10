from .lib.openai_assistant import OpenAIAssistant

class Reviewer:
    def __init__(self, openai_api_key, assistant_id):
        self.assistant = OpenAIAssistant(openai_api_key, assistant_id)
        self.steps = list()

    def add_commit(self, user_message, commit_diff):
        message = f"Commit Message: {user_message}\n\nCommit Diff: {commit_diff}"
        response = self.assistant.add_and_retrieve_message(messages, "user")
        if response and response != 'APIError: No response':
            return response
        return None

    def append_commit(self, user_message="", commit_diff=""):
        self.__append_step(self.add_commit, user_message, commit_diff)

    def execute(self, callback):
        for step in self.steps:
            response = step()
            callback(response)

    def __append_step(self, func, *args, **kwargs):
        def wrapper(*args2, **kwargs2):
            print(f"Running step: {func.__name__}")
            func(*args, **kwargs)

        self.steps.append(wrapper)

