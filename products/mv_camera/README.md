# Machine Vision Camera

Building a photo dataset to train a vision capture model requires to go into the field and capture data.
The process of taking pictures, uploading them by one on an AWS S3 bucket requires many steps.

With MV Camera, the user takes a picture. The photo is instantly uploaded to a common AWS S3 bucket.
Photos are ready to be annotated in label studio.

## Requirements

* python 3
* pipenv
* npm

## Getting started

```bash
make install_requirements_dev
make start
```
