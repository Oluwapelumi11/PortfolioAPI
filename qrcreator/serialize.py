from rest_framework import serializers
from marshmallow import Schema, fields, validate

class QrCodeSerializer(serializers.Serializer):
    data = serializers.CharField(required=True)
    fill_color = serializers.CharField(default="black")
    back_color = serializers.CharField(default="white")

class QrCodeSchema(Schema):
    data = fields.String(required=True, validate=validate.Length(min=1))
    fill_color = fields.String(missing="black")
    back_color = fields.String(missing="white")
