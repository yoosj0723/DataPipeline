import os
import boto3
from datetime import datetime
from botocore.exceptions import NoCredentialsError

# s3 설정
session = boto3.Session(profile_name = 'default')
s3 = session.client('s3')

# 변수 설정
local_folder_path = "/Users/yoosj/Desktop/testS3"
bucket_name = "datapipe2024"
is_public = 1   # 1: public 설정 o, 0: 설정x

# 현재 기준 YYYYMMDD폴더 생성 및 지정위해 경로 설정
def getBucketFolderName():
    current_time = datetime.now()
    target_folder_name = current_time.strftime("%Y%m%d")

    return target_folder_name


def upload_folder(local_folder_path, bucket_name):

    target_folder_name = getBucketFolderName()

    for root, dirs, files in os.walk(local_folder_path):
        for file in files:
            s3_key = f"{target_folder_name}/{file}"

            try:
                file_path = os.path.join(root, file)
                s3.upload_file(file_path, bucket_name, s3_key)

                if is_public:
                    s3.put_object_acl(ACL='public-read', Bucket=bucket_name, Key = s3_key)
            
            except FileNotFoundError:
                print(f"{file_path}를 찾을 수 없습니다")
            except NoCredentialsError:
                print("Not found: Credentials")

upload_folder(local_folder_path, bucket_name)