import os
import boto3
import time


bucket_name = "datapipe2024"
target_file_name = ""	# 올릴 파일

session = boto3.Session(profile_name = 'default')
s3 = session.client('s3')

s3.put_object_acl(ACL='public-read', Bucket=bucket_name, Key = target_file_name)
