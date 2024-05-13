import functools
import logging

def handle_errors(default_value=None):
    """A decorator to handle exceptions in methods and optionally return a default value."""
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            try:
                return func(*args, **kwargs)
            except Exception as e:
                logging.error(f"An error occurred in {func.__name__}: {str(e)}")
                if default_value is not None:
                    return default_value
                raise  # Optionally re-raise the exception if no default value is provided
        return wrapper
    return decorator
