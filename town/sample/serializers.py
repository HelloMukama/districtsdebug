from rest_framework import serializers
from rest_framework.reverse import reverse

from .models import District, Town

from rest_framework import serializers
from rest_framework.reverse import reverse


class TownSerializer(serializers.ModelSerializer):
    id = serializers.SerializerMethodField(read_only=True)
    name = serializers.CharField(read_only=True)

    class Meta:
        model = Town
        fields = ("__all__" )

    def get_id(self, obj):
        if not hasattr(obj, "pk"):
            return None
        if not isinstance(obj, District):
            return None
        return obj.pk


class DistrictSerializer(serializers.ModelSerializer):
    extra_fields = ('goals',)
    id = serializers.SerializerMethodField(read_only=True)
    town = TownSerializer(many=False, read_only=True)
    # total_goals = serializers.SerializerMethodField()

    class Meta:
        model = District
        fields = ("__all__" )

    def get_id(self, obj):
        if not hasattr(obj, "pk"):
            return None
        if not isinstance(obj, District):
            return None
        return obj.pk
 