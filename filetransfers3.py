import boto3
import json

s3 = boto3.client("s3")


def lambda_handler(event, context):
  #s3 = boto3.resource('s3')
  copy_source = {
    'Bucket': 'bucketawsa',
    'Key': 'SF 180.pdf'
  }
  s3.copy(copy_source, 'bucketawsb', 'target.pdf')
