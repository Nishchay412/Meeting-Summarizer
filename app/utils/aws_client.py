import boto3

s3_client = boto3.client('s3', region_name='eu-north-1')
transcribe_client = boto3.client("transcribe", region_name="eu-north-1")