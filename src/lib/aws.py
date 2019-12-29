import os
import boto3
from io import BytesIO


class AWS(object):
    def __init__(self, 
               type='s3',
               region=os.getenv('aws_region_name'),
               key_id=os.getenv('aws_key_id'),
               access_key=os.getenv('aws_access_key'),
               bucket='bo-infra-backup'):
        self.region_name = region
        self.bucket_name = bucket

        self.session = boto3.Session(
            aws_access_key_id=key_id,
            aws_secret_access_key=access_key)

    def init(self, type='s3', obj='resource'):
        if obj == 'resource':
            return self.session.resource(type, region_name=self.region_name)
        elif obj == 'client':
            return self.session.client(type, region_name=self.region_name)

    def s3_download(self, file, output):
        s3 = self.init(type='s3', obj='resource')
        file_stream = BytesIO()

        s3.Object(self.bucket_name, file).download_file(output)
        s3.Object(self.bucket_name, file).download_fileobj(file_stream)

    def s3_upload_file(self, file_in, file_out):
        s3 = self.init(type='s3', obj='resource')

        s3.Bucket(self.bucket_name).upload_file(Filename=file_in, Key=file_out)

    def s3_upload_data(self, data, filename):
        s3 = self.init(type='s3', obj='resource')

        s3.Object(self.bucket_name, filename).put(Body=data)

