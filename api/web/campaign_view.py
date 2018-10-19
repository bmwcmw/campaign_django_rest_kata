from rest_framework import viewsets

from api.model.campaign import Campaign
from api.web.campaign_serializer import CampaignSerializer


class CampaignViewSet(viewsets.ModelViewSet):
    """
    This viewset automatically provides `list`, `create`, `retrieve`,
    `update` and `destroy` actions.

    Additionally we also provide an extra `highlight` action.
    """
    queryset = Campaign.objects.all()
    serializer_class = CampaignSerializer

    # Should override if do not install rest_framework app
    #
    # def list(self, request, **kwargs):
    #     serializer = CampaignSerializer(self.queryset, many=True)
    #     return JsonResponse(serializer.data, safe=False)
    #
    # def retrieve(self, request, pk=None, **kwargs):
    #     user = get_object_or_404(self.queryset, pk=pk)
    #     serializer = CampaignSerializer(user)
    #     return JsonResponse(serializer.data, safe=False)
