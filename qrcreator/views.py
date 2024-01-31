from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serialize import QrCodeSerializer, QrCodeSchema
import qrcode

class GenerateQrCode(APIView):
    def get(self, request, *args, **kwargs):
        # Deserialize input from the request
        serializer = QrCodeSerializer(data=request.query_params)
        serializer.is_valid(raise_exception=True)
        params = serializer.validated_data

        # Generate QR code using the provided or default values
        qr_schema = QrCodeSchema()
        qr_params = qr_schema.load(params)

        qr = qrcode.QRCode(
            version=1,
            error_correction=qrcode.constants.ERROR_CORRECT_L,
            box_size=10,
            border=4,
        )
        qr.add_data(qr_params['data'])
        qr.make(fit=True)

        img = qr.make_image(fill_color=qr_params['fill_color'], back_color=qr_params['back_color'])

        # Serve the image directly
        response = Response(content_type="image/png")
        img.save(response, format="PNG")
        return response
