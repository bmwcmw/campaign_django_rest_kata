from django.contrib.admin import site

from api.model.campaign import Campaign
from api.model.operation import Operation

site.register(Campaign)
site.register(Operation)
