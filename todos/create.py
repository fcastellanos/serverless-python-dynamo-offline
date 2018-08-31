import json
import logging
import os
import time
import uuid

import boto3

from todos import db_utils

def create(event, context):
    dynamodb = db_utils.db_picker(event)

    data = json.loads(event['body'])
    if 'activity_title' not in data:
        logging.error("Validation Failed")
        raise Exception("Couldn't create the todo item.")
        return

    timestamp = int(time.time() * 1000)

    table = dynamodb.Table(os.environ['DYNAMODB_TABLE'])

    item = {
        'id': str(uuid.uuid1()),
        'activity_title': data['activity_title'],
        'activity_description': data['activity_description'],
        'date': data['date'],
        'time': data['time'],
        'period': data['period'],
        'checked': False,
        'createdAt': timestamp,
        'updatedAt': timestamp,
    }

    # write the todo to the database
    table.put_item(Item=item)

    # create a response
    response = {
        "statusCode": 200,
        "body": json.dumps(item),
        "headers": {
            "Content-Type": "application/json",
            "Access-Control-Allow-Origin": "*"
        }
    }

    return response
