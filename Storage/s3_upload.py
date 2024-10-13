import os
import boto3
import time


bucket_name = "datapipe2024"
file_name = ""	# 파일명
target_file_name = ""	# 올릴 파일
local_file_path = os.getcwd() + "/"+ file_name	# 현재 폴더명

session = boto3.Session(profile_name = 'default')
s3 = session.client('s3')

s3.upload_file(local_file_path, bucket_name, target_file_name)
