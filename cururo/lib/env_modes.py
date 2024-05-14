import functools

class EnvModes:
    allowed_modes = ['production', 'development', 'testing']

    def __init__(self, mode='production') -> None:
        self.mode = mode
        self.validate_mode()

    def validate_mode(self):
        message = f"Mode must be one of {self.allowed_modes}"
        assert self.mode in self.allowed_modes, message

    def __call__(self, mode: str) -> None:
        self.mode = mode
        self.validate_mode()

    def __str__(self) -> str:
        return f"{self.__class__.__name__}(mode={self.mode})"
    
    def __repr__(self) -> str:
        return f"{self.__class__.__name__}(mode={self.mode})"
        
    def __enter__(self):
        return self
    
    @staticmethod
    def non_production_handler(return_value=None):
        """Decorator to handle non-production specific logic."""
        def decorator(func):
            @functools.wraps(func)
            def wrapper(self, *args, **kwargs):
                if self.mode != 'production':
                    return return_value
                return func(self, *args, **kwargs)
            return wrapper
        return decorator
        