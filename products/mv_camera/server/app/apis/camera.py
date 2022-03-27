import logging
import urllib
import uuid

import boto3
from flask_restx import Namespace, Resource, fields, marshal

from server.app.storage.cloud import CloudStorageRepository

api = Namespace('camera', description='publish camera image to s3')

"""
The exposition model we are using.
"""
photo_model = api.model('Photo', {
    'dataUri': fields.String(required=True, description='The data uri of png image')
})

notification_model = api.model('Notification', {
    'message': fields.String(description='the message of notification'),
    'title': fields.String(required=True, description='title notification'),
    'type': fields.String(required=True, description='the type of notification, either danger, success, warning, info '),
})


@api.route('/photo')
class CameraPhoto(Resource):

    @api.expect(photo_model)
    @api.response(200, 'Success', notification_model)
    def post(self):
        try:
            storage_repository = CloudStorageRepository()

            _photo = api.payload
            response = urllib.request.urlopen(_photo['dataUri'])

            storage_repository.upload(response.file, f"{uuid.uuid4().hex}.png")

            return marshal({
                'title': 'picture is uploaded in cloud storage',
                'type': 'success',
            }, notification_model), 201
        except Exception as exception:
            logging.exception(exception)
            return marshal({
                'title': 'failed to upload picture in cloud storage',
                'type': 'danger',
            }, notification_model), 201
