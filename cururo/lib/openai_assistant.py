import time
from openai import OpenAI
from .ai_env import AIEnv, EnvModes, dummy_content
from ..util.util import handle_errors

class OpenAIAssistant(AIEnv):
    def __init__(self, api_key, assistant_id, thread_id=None, mode='production'):
        super().__init__(mode)
        self.client = OpenAI(api_key=api_key)
        self.assistant_id = assistant_id

        self.thread_id = thread_id if thread_id else self.__create_thread()

    @EnvModes.non_production_handler('non_prod')
    @handle_errors(default_value='Failed to create thread')
    def __create_thread(self):
        response = self.client.beta.threads.create()
        return response.id
    
    @EnvModes.non_production_handler({'id': 'non_prod', **dummy_content})
    @handle_errors(default_value='Failed to add message')
    def add_message(self, message, role):
        return self.client.beta.threads.messages.create(
            thread_id=self.thread_id,
            role=role,
            content=message
        )
    
    @EnvModes.non_production_handler({'data': [dummy_content]})
    @handle_errors(default_value='Failed to get messages list')
    def get_messages_list(self):
        return self.client.beta.threads.messages.list(thread_id=self.thread_id)
    
    @EnvModes.non_production_handler(dummy_content)
    @handle_errors(default_value='Failed to get last message')
    def get_last_message(self):
        return self.get_messages_list().data[0]
    
    @EnvModes.non_production_handler({'id': 'non_prod'})
    @handle_errors(default_value='Failed to create thread run')
    def create_thread_run(self):
        return self.client.beta.threads.runs.create(
            thread_id=self.thread_id,
            assistant_id=self.assistant_id,
        )
    
    @EnvModes.non_production_handler({'id': 'non_prod', 'status': 'completed'})
    @handle_errors(default_value='Failed to wait on run')
    def wait_on_run(self, run):
        while run.status == "queued" or run.status == "in_progress":
            run = self.client.beta.threads.runs.retrieve(
                thread_id=self.thread_id,
                run_id=run.id,
            )
            time.sleep(0.5)
        return run
    
    @EnvModes.non_production_handler('Hello, world!')
    @handle_errors(default_value='APIError: no response')
    def add_and_retrieve_message(self, message, role):
        message = self.add_message(message, role)
        run = self.create_thread_run()
        status = self.wait_on_run(run)
        msg = self.get_last_message()
        return msg.content[0].text.value
    
if __name__ == '__main__':
    assistant = OpenAIAssistant('a', 'b', mode='development')
    print(assistant.add_and_retrieve_message('Hello, world!', 'user'))