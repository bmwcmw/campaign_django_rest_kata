from rest_framework import viewsets

from api.model.operation import Operation
from api.web.operation_serializer import OperationSerializer


class OperationViewSet(viewsets.ModelViewSet):
    """
    This viewset automatically provides `list`, `create`, `retrieve`,
    `update` and `destroy` actions.

    Additionally we also provide an extra `highlight` action.
    """
    queryset = Operation.objects.all()
    serializer_class = OperationSerializer
