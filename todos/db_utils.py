
def db_picker(event):
    import boto3
    
    if event["isOffline"]:
        return boto3.resource('dynamodb', endpoint_url='http://localhost:8000')
    else:
        return boto3.resource('dynamodb')
