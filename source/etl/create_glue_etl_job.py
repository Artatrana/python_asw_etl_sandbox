import sys
import boto3
glue_client = boto3.client('glue', region_name='us-west-2')

job_name = 'arta-first-glue-job'
role_name = 'AWSGlueServiceRoleDefault'  # Replace with your role name
script_location = 's3://my-bucket/scripts/my_glue_script.py'

response = glue_client.create_job(
    name=job_name,
    Role=role_name,
    ExecutionProperty={'MaxConcurrentRuns': 1},
    Command={
        'Name':'glueetl',
        'ScriptLocation': script_location,
        'PythonVersion': '3'
    },
    DefaultArguments={'--TempDir': 's3://my-bucket/temp/',
        '--job-language': 'python'
    },
    MaxRetries=0,
    GlueVersion='3.0',  # or '4.0' depending on your use case
    NumberOfWorkers=2,
    WorkerType='Standard'
)
print(f"✅ Glue Job '{job_name}' created successfully.")
