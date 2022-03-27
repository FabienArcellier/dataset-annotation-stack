from flask_restx import Api

from app.apis.camera import api as camera

api = Api(
    title='api',
    version='1.0',
    description='',
    prefix='/api',
    doc='/api'
)

api.add_namespace(camera)
