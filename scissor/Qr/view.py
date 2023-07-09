import qrcode
from flask_restx import Namespace, Resource
from flask import request, send_file

from io import BytesIO



Qr_code= Namespace('Qr_code', description="a namespace for QrCode")

@Qr_code.route('/Qrcode')
class QrCode(Resource):
    def post(self):
        buffer = BytesIO()
        data = request.form.get('data')


        image = qrcode.make(data)
        image.save(buffer)
        buffer.seek(0)
        

        response = send_file(buffer, ninetype= 'image/png')
        return response