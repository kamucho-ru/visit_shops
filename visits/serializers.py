from rest_framework import serializers

from visits.models import Outlet, Visit


class OutletSerializer(serializers.ModelSerializer):
    class Meta:
        model = Outlet
        fields = ("id", "title")


class VisitSerializer(serializers.ModelSerializer):
    class Meta:
        model = Visit
        fields = ("id", "datetime")
