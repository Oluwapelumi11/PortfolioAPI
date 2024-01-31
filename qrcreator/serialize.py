from rest_framework import serializers
from marshmallow import Schema, fields, validate

class QrCodeSerializer(serializers.Serializer):
    data = serializers.CharField(required=True)
    fill = serializers.CharField(default="black")
    back = serializers.CharField(default="white")

class QrCodeSchema(Schema):
    data = fields.String(required=True, validate=validate.Length(min=1))
    fill = fields.String(missing="black")
    back = fields.String(missing="white")
