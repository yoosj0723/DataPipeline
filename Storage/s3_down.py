import os
import boto3
import time


bucket_name = "datapipe2024"
folder_name = ""	# 폴더명
path = ""	# 파일명

session = boto3.Session(profile_name = 'default')
s3 = session.client('s3')

print(folder_name + os.path.basename(path))

s3.download_file(bucket_name, folder_name+os.path.basename(path), "./"+os.path.basename(path))
