from rest_framework import serializers
from .models import Product
from PIL import Image
from io import BytesIO
from django.core.files.base import ContentFile

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['id','name', 'category', 'price', 'description', 'stars', 'image']

    def validate_image(self, image):
        img = Image.open(image)
        if img.format not in ['JPEG', 'PNG']:
            raise serializers.ValidationError('Image must be either JPEG or PNG format.')
        return image

    def create(self, validated_data):
        image = validated_data.pop('image', None)
        if image:
            img = Image.open(image)
            buffer = BytesIO()
            img.save(buffer, format=img.format)
            image_file = ContentFile(buffer.getvalue())
            validated_data['image'] = image_file

        return super().create(validated_data)

    def update(self, instance, validated_data):
        image = validated_data.pop('image', None)
        if image:
            img = Image.open(image)
            buffer = BytesIO()
            img.save(buffer, format=img.format)
            image_file = ContentFile(buffer.getvalue())
            validated_data['image'] = image_file

        return super().update(instance, validated_data)

