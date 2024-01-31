from django.http import HttpResponse
from rest_framework.views import APIView
from rest_framework.response import Response
from qrcode_generator.serializers import QrCodeSerializer, QrCodeSchema
import qrcode
from io import BytesIO

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

        # Save the image to a BytesIO buffer
        image_buffer = BytesIO()
        img.save(image_buffer, format="PNG")
        image_data = image_buffer.getvalue()

        # Set HTTP headers for download
        response = HttpResponse(image_data, content_type="image/png")
        response['Content-Disposition'] = 'attachment; filename="qrcode.png"'

        return response
