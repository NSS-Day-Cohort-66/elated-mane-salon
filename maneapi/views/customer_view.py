"""View module for handling requests about customers"""
from rest_framework import serializers, status
from rest_framework.response import Response
from rest_framework.viewsets import ViewSet
from django.contrib.auth.models import User
from maneapi.models import Customer, HairStyle


class CustomerView(ViewSet):
    """Viewset for customers"""

    def update(self, request, pk=None):
        """Handle PUT requests for a customer

        Returns:
            Response -- Empty body with 204 status code
        """
        name = request.data["name"]

        customer = Customer.objects.get(pk=pk)
        customer.style = HairStyle.objects.get(pk=request.data["style_id"])
        customer.name = name
        customer.save()

        return Response(None, status=status.HTTP_204_NO_CONTENT)

    def retrieve(self, request, pk=None):
        """Handle GET requests for single game

        Returns:
            Response -- JSON serialized game instance
        """
        customer = Customer.objects.get(pk=pk)
        serialized = CustomerSerializer(customer)
        return Response(serialized.data)


    def list(self, request):
        """Handle GET requests to customers resource

        Returns:
            Response -- JSON serialized list of customers
        """
        customers = Customer.objects.all()
        serialized = CustomerSerializer(customers, many=True)
        return Response(serialized.data)

    def create(self, request):
        """Handle POST operations for customers

        Returns:
            Response -- JSON serialized customer instance
        """
        customer = Customer()
        customer.name = request.data["name"]
        customer.style = HairStyle.objects.get(pk=request.data["style_id"])
        customer.save()

        serialized = CustomerSerializer(customer, context={'request': request})
        return Response(serialized.data, status=status.HTTP_201_CREATED)


class CustomerStylistSerializer(serializers.ModelSerializer):
    full_name = serializers.SerializerMethodField()

    def get_full_name(self, obj):
        return f'{obj.first_name} {obj.last_name}'

    class Meta:
        """JSON serializer for customer creator"""
        model = User
        fields = ('id', 'full_name', 'clients')


class CustomerSerializer(serializers.ModelSerializer):
    """JSON serializer for customer creator"""
    stylists = CustomerStylistSerializer(many=True)

    class Meta:
        """JSON serializer for customer creator"""
        model = Customer
        fields = ('id', 'stylists', 'name', 'date_created',)
