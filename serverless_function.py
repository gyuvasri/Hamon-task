import boto3
import os
from dotenv import load_dotenv

load_dotenv()

aws_access_key_id = os.getenv("AWS_ACCESS_KEY_ID")
aws_secret_access_key = os.getenv("AWS_SECRET_ACCESS_KEY")
aws_s3_bucket = os.getenv("AWS_S3_BUCKET")

def lambda_handler(event, context):
    print("Serverless function executed.")
