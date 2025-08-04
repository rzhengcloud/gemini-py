import time
from dataclasses import dataclass



#@dataclass
class User:
    def __init__(self):
        pass
    def __init__(self, name: str, age: int = None):

        pass
        self.name = name
        self.age = age
    #  def __repr__(self):
        # return f"User(name={self.name}, age={self.age})"
    # name: str
    # age: int
    
# 1. Define the decorator function
def timer_decorator(func):
    """
    This is our decorator. It takes a function 'func' as an argument.
    """
    def wrapper(*args, **kwargs):
        """
        The 'wrapper' function is what actually replaces the original function.
        It can accept any arguments (*args, **kwargs) that the original function might take.
        """
        start_time = time.time()  # Record the start time
        result = func(*args, **kwargs)  # Call the original function
        end_time = time.time()    # Record the end time
        execution_time = end_time - start_time
        print(f"'{func.__name__}' executed in {execution_time:.4f} seconds.")
        return result  # Return the result of the original function

    return wrapper # The decorator returns the wrapper function

# 2. Apply the decorator using the '@' syntax
@timer_decorator
def long_running_function():
    """
    An example function that simulates some work.
    """
    print("Starting long_running_function...")
    time.sleep(2)  # Pause for 2 seconds to simulate work
    print("Finished long_running_function.")
    return "Data processed successfully!"

@timer_decorator
def another_function(name):
    """
    Another function to demonstrate the decorator with arguments.
    """
    print(f"Hello, {name}! Doing some quick work...")
    time.sleep(0.5)
    return f"Greetings from {name}!"


@timer_decorator
def process_user(user: User):
    print(f"Processing user: {user.name}, Age: {user.age}")
    time.sleep(1)
    return f"Processed {user.name}."

# 3. Call the decorated functions
# print("\n--- Calling long_running_function ---")
# returned_data = long_running_function()
# print(f"Result: {returned_data}")

# print("\n--- Calling another_function ---")
# message = another_function("Alice")
# print(f"Message: {message}")

