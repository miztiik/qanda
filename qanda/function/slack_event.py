"""Process a slack event."""
from pprint import pprint


def lambda_handler(event, context):
    print("evt got invoked!")
    pprint(event)
    pprint(context)


3