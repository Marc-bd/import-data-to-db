from .serializers import DataSerializer
from import_data.models import Data
from rest_framework.views import APIView

import ipdb


class DataView(APIView):
    queryset = Data.objects.all()
    serializer_class = DataSerializer
