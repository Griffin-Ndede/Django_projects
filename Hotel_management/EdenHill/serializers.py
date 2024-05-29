# import serializer from rest_framework
from rest_framework import serializers

# import model from models.py
from .models import Users

# Create a model serializer
class EdenHillSerializer(serializers.HyperlinkedModelSerializer):
	# specify model and fields
	class Meta:
		model = Users
		fields = ('firstname', 'age')
