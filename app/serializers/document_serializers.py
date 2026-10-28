from rest_framework import serializers
from app.models.document import Document

class DocumentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Document
        fields = ['id', 'title', 'content', 'uploaded_at', 'owner']
        read_only_fields = ['id', 'uploaded_at', 'owner']
