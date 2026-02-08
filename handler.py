import json

def hello(event, context):
    body = {
        "message": "Hi Shubham, Welcome!"
    }
    return {
        "statusCode": 200,
        "body": json.dumps(body)
    }

def bye(event, context):
    body = {
        "message": "3... 2... 1... Bye"
    }
    return {
        "statusCode": 200,
        "body": json.dumps(body)
    }
