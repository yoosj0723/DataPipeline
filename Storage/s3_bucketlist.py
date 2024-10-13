import os
import boto3
import time

session = boto3.Session(profile_name = 'default')
s3 = session.client('s3')

response = s3.list_buckets()

print('Existing buckets: ')
for bucket in response['Buckets']:
    print(f'    {bucket['Name']}')