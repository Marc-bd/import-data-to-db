from rest_framework import serializers
from .models import Data
from .utils.read_text import read_text
import json


class DataSerializer(serializers.ModelSerializer):

    data = serializers.SerializerMethodField()

    class Meta:

        model = Data
        fields = ["id", "file", "data"]

    def get_data(self, obj):

        return "aaa"
