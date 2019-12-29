#!/usr/bin/env python
# -*- encoding: utf-8
import os
import requests

from lib.aws import AWS
from lib.opencv import OpenCV
from lib.gcp import GCP

from dotenv import load_dotenv
load_dotenv()


def main(my_date):
    # my_date = "29/11/2019"

    # Instancies
    aws = AWS(bucket=os.getenv('aws_s3_bucket'))
    gcp = GCP(cred_file=os.getenv('gcp_token_file'))
    cv = OpenCV()

    # Get list of photos
    photos = gcp.listMedia(date_filter=my_date, media_type=["PHOTO"])
    if photos is None:
        print('error', 'No photos found, exit')
        exit(0)
    print('{} photos found'.format(len(photos)))

    # For each photo: download, extract each face and store individual face in S3
    face_catalog = []
    for photo in photos:
        # Download photo data
        photo_data = requests.get(photo['baseUrl']).content
        with open(photo['filename'], 'wb') as handler:
            handler.write(photo_data)

        faces = cv.extract_faces(photo['filename'])
        #faces = cv.extract_faces_from_buffer(photo_data)

        i_face = 1
        for face in faces:
            filename = 'extract/{}'.format(face)

            aws.s3_upload_file(face, filename)
            os.remove(face)
            #aws.s3_upload_data(face, filename)

            face = dict(photo)
            face['face_id'] = i_face
            face['face_filename'] = filename
            #del face['baseUrl']
            face_catalog.append(face)

            i_face = i_face + 1

        os.remove(photo['filename'])
        print('{} face(s) found in the photo {}'.format(i_face - 1, photo['filename']))

    if face_catalog:
        for face in face_catalog:
            print('JSON catalog of faces\n{}'.format(face))
        print('{} face(s) found in total'.format(len(face_catalog)))
    else:
        print('No face found :(')


if __name__ == '__main__':
    main(os.getenv('my_date'))

