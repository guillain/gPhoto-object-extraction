# gPhoto-object-extraction
_How to run easily the object recognition_

For the demo and to make it more funny:
- the source of information (means the photo galery) is *Google Photo*!
- the object recognized are stored on *AWS S3*!
- all run in docker :)
- ... compatible with Raspberry 

## Pre-requisite
- Docker host
- Internet access

## Easy Run
After have cloned the repository localy (`git clone https://github.com/guillain/gPhoto-object-extraction`)
and enter in the new directory (`cd gPhoto-object-extraction`) execute the following commands:

1/ create your own confguration file: 
  - `cp sample.env .env && vi .env` and add your AWS credentials info
  - import the files `google-photo.json` and `google-photo-token.json` as GCP credentials info
  - if you need to run it on Raspberry, invert the comment on the first two lines in the `Dockerfile`

2/ execute the container with the desired date for your Google Photos: `./run "29/12/2019"`


## Support
- Original post:
  - https://www.hackster.io/mjrobot/real-time-face-recognition-an-end-to-end-project-a10826
  - https://github.com/Mjrovai/OpenCV-Face-Recognition
- Raspberry: https://www.raspberrypi.org
- Docker: https://www.docker.com
- OpenCV: https://opencv.org
