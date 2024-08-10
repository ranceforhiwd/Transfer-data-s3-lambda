import boto3
brian = boto3.client("s3")
#S3_BUCKET = 'bucketawsa'

def lambda_handler(event, context):
  # Retrieve the list of existing buckets
  #s3 = boto3.client('s3')
  response = brian.list_objects(Bucket='bucketawsa')
  print(response)
  #exit()
  # Brian2 Output the bucket names
  #print('Existing buckets:')
  for bucket in response['Contents']:
    a = list(bucket.values())
    print(a[0])