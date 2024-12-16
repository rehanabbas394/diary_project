from rest_framework import serializers
from .models import DiaryEntry

class DiaryEntrySerializer(serializers.ModelSerializer):
    user = serializers.ReadOnlyField(source='user.username')

    
    class Meta:
        model = DiaryEntry
        fields = '__all__'
