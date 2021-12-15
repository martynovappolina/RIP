from cd.models import CD_lib
from cd.models import CD
from rest_framework import serializers


class CDSerializer(serializers.ModelSerializer):
    class Meta:
        model = CD
        fields = ["id", "name", "capacity", "cdLib"]

class CDLibSerializer(serializers.ModelSerializer):
    class Meta:
        model = CD_lib
        fields = ["id", "name"]

