from rest_framework import serializers

from api.model.campaign import Campaign
from api.web.operation_serializer import OperationSerializer


class CampaignSerializer(serializers.ModelSerializer):
    # Have the _set name of model field
    operation_set = OperationSerializer(many=True, read_only=True)

    class Meta:
        model = Campaign
        fields = ('read_only_name', 'name', 'operation_set')
        read_only_fields = ('read_only_name',)
