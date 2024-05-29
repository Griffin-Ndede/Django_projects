# import viewsets
from rest_framework import viewsets

# import local data
from .serializers import EdenHillSerializer
from .models import Users

# create a viewset


class EdenHillViewSet(viewsets.ModelViewSet):
	# define queryset
	queryset = Users.objects.all()

	# specify serializer to be used
	serializer_class = EdenHillSerializer
