import os
import boto3
import time


bucket_name = "datapipe2024"
download_directory = "/Users/yoosj/Desktop/test_downS3"

session = boto3.Session(profile_name = 'default')
s3 = session.client('s3')

def download_all_from_s3(s3, bucket_name, download_directory):
    try:
        # S3 버킷의 모든 객체 리스트 가져오기
        response = s3.list_objects_v2(Bucket=bucket_name)

        if 'Contents' not in response:
            print("S3 버킷이 비어있습니다.")
            return

        # 모든 파일 다운로드
        for obj in response['Contents']:
            file_name = obj['Key']
            local_file_path = os.path.join(download_directory, os.path.basename(file_name))

            s3.download_file(bucket_name, file_name, local_file_path)

            print(f"다운로드 완료: s3://{bucket_name}/{file_name} -> {local_file_path}")

    except Exception as e:
        print(f"S3 다운로드 중 오류 발생: {str(e)}")

download_all_from_s3(s3, bucket_name, download_directory)