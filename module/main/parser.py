
import os
import sys
import re
import json

from .myclass import ThisIsMe


def main(lambda_args={}):
    """This function is called when run as python3 -m ${MODULE}
    Parse any additional arguments and call required module functions."""

    # invoked from current host
    import argparse

    module_name = __loader__.name.split('.')[0]
    
    parser = argparse.ArgumentParser(
        prog=module_name,
        description="This is my new shiny pip package called: " + module_name,
    )

    parser.add_argument('--test', action='store_true', required=True,
                        help='Do a test run.')
    parser.add_argument('--name', action='store', nargs=1, required=False, type=str,
                        default=['dummy'],
                        help='Optionally add your name.')

    args = parser.parse_args(sys.argv[1:])

    if args.test:
        # expecting one argument
        if isinstance(args.name, list) and isinstance(args.name[0], str):
            name = args.name[0]
        print('testme')
        #instance = MyOwnClass()
        #instance.update_name(name=name)
        #print(instance.say_hello())
