import boto3
import json

ec2 = boto3.client('ec2')
def lambda_handler(event, context):
    response = ec2.describe_availability_zones()
    ack = "The Deployment is Sucessful xD"
    print(ack)
    return {"statusCode": 200, "body": json.dumps(response),"message":ack}
