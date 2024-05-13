from typing import Any
from .env_modes import EnvModes

dummy_content = {'content': [{'text': {'value': 'Hello, world!'}}]}

class AIEnv(EnvModes):

    def __init__(self, mode='production', *args, **kwargs) -> None:
        super().__init__(mode)

    @EnvModes.non_production_handler({'id': 'non_prod', **dummy_content})
    def add_message(self, message, role):
        return "Funciona para todo ambiente"

    @EnvModes.non_production_handler({'data': [dummy_content]})
    def get_messages_list(self):
        return []
    
    @EnvModes.non_production_handler(dummy_content)
    def get_last_message(self):
        return {}

    @EnvModes.non_production_handler({'id': 'non_prod'})   
    def create_thread_run(self):
        return {'id': 'prod'}

    @EnvModes.non_production_handler({'id': 'non_prod', 'status': 'completed'})
    def wait_on_run(self, run):
        return {'id': 'non_prod', 'status': 'completed'}

    @EnvModes.non_production_handler('Hello, world!')
    def add_and_retrieve_message(self, message, role):
        return 'Hello, world!'
    


if __name__ == '__main__':
    ai_env_dev = AIEnv(mode='development')
    print(ai_env_dev.add_message('Hello, world!', 'user'))
    ai_env = AIEnv(mode='production')
    print(ai_env.add_message('Hello, world!', 'user'))
