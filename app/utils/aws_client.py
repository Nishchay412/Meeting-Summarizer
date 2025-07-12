import boto3
#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

s3_client = boto3.client('s3', region_name='eu-north-1')
transcribe_client = boto3.client("transcribe", region_name="eu-north-1")