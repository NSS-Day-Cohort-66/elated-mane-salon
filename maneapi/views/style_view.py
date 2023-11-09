"""View module for handling requests about styles"""
from rest_framework import serializers, status
from rest_framework.response import Response
from rest_framework.viewsets import ViewSet
from django.contrib.auth.models import User
from maneapi.models import HairStyle, Customer


class StyleView(ViewSet):
    """Viewset for styles"""

    def retrieve(self, request, pk=None):
        """Handle GET requests for single game

        Returns:
            Response -- JSON serialized game instance
        """
        style = HairStyle.objects.get(pk=pk)
        serialized = StyleSerializer(style)
        return Response(serialized.data)

    def list(self, request):
        """Handle GET requests to styles resource

        Returns:
            Response -- JSON serialized list of styles
        """
        styles = HairStyle.objects.all()
        serialized = StyleSerializer(styles, many=True)
        return Response(serialized.data)


class StyleCustomerSerializer(serializers.ModelSerializer):
    """JSON serializer for style creator"""

    class Meta:
        """JSON serializer for style creator"""
        model = Customer
        fields = ( 'id', 'name',  )

class StyleSerializer(serializers.ModelSerializer):
    """JSON serializer for style creator"""
    customers = StyleCustomerSerializer(many=True)

    class Meta:
        """JSON serializer for style creator"""
        model = HairStyle
        fields = ( 'id', 'label', 'customers', )
