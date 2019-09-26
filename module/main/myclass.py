"""
THIS SPECIFIC FILE IS DISTRIBUTED UNDER THE UNLICENSE: http://unlicense.org.

THIS MEANS YOU CAN USE THIS CODE EXAMPLE TO KICKSTART A PROJECT YOUR OWN.
AFTER YOU CREATED YOUR OWN ORIGINAL WORK, YOU CAN REPLACE THIS HEADER :)
"""

class ThisIsMe:
    """Example class for education and testing."""
    def __init__(self, name=None):
        self.name = name

    def update_name(self, name):
        """Reset name attribute."""
        if not isinstance(name, str):
            print('That is not a string! Refusing to update.')
        else:
            self.name = name
        return self

    def say_hello(self):
        """Return name attribute."""
        if not isinstance(self.name, str):
            return str('Cant say hi because I dont know your name yet.')
        return str('Hi ' + self.name + '!')

    # add more fun stuff here
