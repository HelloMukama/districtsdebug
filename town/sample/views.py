from rest_framework import viewsets, generics, mixins, throttling


from .models import City, TownType, Town, District
from .serializers import DistrictSerializer, TownSerializer


# class DistrictViewSet(FilteredListModelMixin, viewsets.ReadOnlyModelViewSet):
#     # permission_classes = [permissions.IsAuthenticatedOrReadOnly,]
#     serializer_class = DistrictSerializer
#     queryset = District.objects.filter(town__isnull=False).order_by('-date_made')
#     # filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
#     ordering_fields = ['date_made', 'town__name']

#     def district(self, request):
#         town_queryset = District.objects.select_related('town__city')
#         serializer = DistrictSerializer(town_queryset, many=True)

#         return Response(serializer.data)


class DistrictListViewSet(generics.ListCreateAPIView):
    queryset = District.objects.all()
    serializer_class = DistrictSerializer

    def get_queryset(self, *args, **kwargs):
        qs = super().get_queryset(*args, **kwargs)
        return qs


class TownsListViewSet(generics.ListCreateAPIView):
    # queryset = Town.objects.filter(is_city=True)
    queryset = Town.objects.filter(is_city=False)
    serializer_class = TownSerializer

    def get_queryset(self, *args, **kwargs):
        qs = super().get_queryset(*args, **kwargs)
        return qs
