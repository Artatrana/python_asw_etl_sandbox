import boto3
from botocore.exceptions import ClientError
from jinja2.bccache import Bucket


def create_s3_bucket(bucket_name, region=None):
    try:
        # Create an S3 client
        if region is None:
            s3_client = boto3.client('s3')
            s3_client.create_bucket(Bucket=bucket_name)
        else:
            s3_client = boto3.client('s3',region_name=region)
            location = {'LocationConstraint': region}
            s3_client.create_bucket(Bucket = bucket_name, CreateBucketConfiguration=location)
        print(f"Bucket '{bucket_name}' created successfully.")
    except ClientError as e:
        print(f"❌ Error creating bucket: {e}")


# Example usage
bucket_name = "artatrana_bucket-test-1"  # Bucket names must be globally unique
region = "us-west-2"  # Change to your desired AWS region

create_s3_bucket('artatest-may1', region)
