"""View module for handling requests about equipments"""
from rest_framework import serializers, status
from rest_framework.response import Response
from rest_framework.viewsets import ViewSet
from django.contrib.auth.models import User
from maneapi.models import Equipment, EquipmentType


class EquipmentView(ViewSet):
    """Viewset for equipments"""

    def update(self, request, pk=None):
        """Handle PUT requests for a equipment

        Returns:
            Response -- Empty body with 204 status code
        """
        equipment = Equipment.objects.get(pk=pk)

        stylist_id = request.data.get("stylist_id", None)
        type = request.data.get("type", None)
        manufacturer = request.data.get("manufacturer", None)
        cost = request.data.get("cost", None)
        purchase_date = request.data.get("purchase_date", None)

        equipment.stylist = User.objects.get(pk=stylist_id)
        equipment.type = EquipmentType.objects.get(pk=type)
        equipment.manufacturer = manufacturer
        equipment.cost = cost
        equipment.purchase_date = purchase_date
        equipment.save()

        return Response(None, status=status.HTTP_204_NO_CONTENT)

    def retrieve(self, request, pk=None):
        """Handle GET requests for single game

        Returns:
            Response -- JSON serialized game instance
        """
        equipment = Equipment.objects.get(pk=pk)
        serialized = EquipmentSerializer(equipment)
        return Response(serialized.data)

    def list(self, request):
        """Handle GET requests to equipments resource

        Returns:
            Response -- JSON serialized list of equipments
        """
        equipments = Equipment.objects.all()
        serialized = EquipmentSerializer(equipments, many=True)
        return Response(serialized.data)

    def create(self, request):
        """Handle POST operations for equipments

        Returns:
            Response -- JSON serialized equipment instance
        """
        stylist_id = request.data.get("stylist_id", None)
        type = request.data.get("type", None)
        manufacturer = request.data.get("manufacturer", None)
        cost = request.data.get("cost", None)
        purchase_date = request.data.get("purchase_date", None)

        equipment = Equipment()
        equipment.stylist = User.objects.get(pk=stylist_id)
        equipment.type = EquipmentType.objects.get(pk=type)
        equipment.manufacturer = manufacturer
        equipment.cost = cost
        equipment.purchase_date = purchase_date
        equipment.save()

        serialized = EquipmentSerializer(
            equipment, context={'request': request})
        return Response(serialized.data, status=status.HTTP_201_CREATED)


class EquipmentTypeSerializer(serializers.ModelSerializer):
    """JSON serializer for equipment creator"""

    class Meta:
        """JSON serializer for equipment creator"""
        model = EquipmentType
        fields = ( 'id', 'label' )

class EquipmentSerializer(serializers.ModelSerializer):
    """JSON serializer for equipment creator"""
    type = EquipmentTypeSerializer(many=False)

    class Meta:
        """JSON serializer for equipment creator"""
        model = Equipment
        fields = (
            'id', 'stylist', 'manufacturer', 'cost',
            'type', 'purchase_date'
        )
