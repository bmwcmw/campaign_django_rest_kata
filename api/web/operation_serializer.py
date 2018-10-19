from rest_framework import serializers

from api.model.campaign import Campaign


class OperationSerializer(serializers.ModelSerializer):
    # Have the same name of model field
    campaign = serializers.SlugRelatedField(
        many=False,
        read_only=True,
        slug_field='name'
    )

    class Meta:
        model = Campaign
        fields = '__all__'
        read_only_fields = ('campaign',)
