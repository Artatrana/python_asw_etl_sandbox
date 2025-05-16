import  boto3
from jinja2.bccache import Bucket


def create_folder_s3(bucket_name, folders):
    s3 =boto3.client('s3')
    for folder in folders:
        key_name =  folder if folder.endswith('/') else folder + '/'
        s3.put_object(Bucket=bucket_name,Key=key_name)
        print(f"✅ Created folder: {key_name}")

# Example usage
bucket_name = 'artatest-may1'
folders = [
    'raw-data/',
    'raw-data/test1/input/',
    'processed-data/',
    'processed-data/test1/output/',
    'logs/',
    'archives/2024/',
    'archives/2025/'
]

create_folder_s3(bucket_name, folders)


