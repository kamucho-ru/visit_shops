from rest_framework import status
from rest_framework.generics import GenericAPIView, get_object_or_404
from rest_framework.response import Response

from visits.models import Outlet, Visit, Worker
from visits.serializers import OutletSerializer, VisitSerializer


class OutletView(GenericAPIView):
    def get(self, request, *args, **kwargs):
        phone = request.headers.get("phone")
        worker = get_object_or_404(Worker.objects, phone_number=phone)
        return Response(
            OutletSerializer(worker.outlets.all(), many=True).data, status=status.HTTP_200_OK
        )

    def post(self, request, *args, **kwargs):
        phone = request.headers.get("phone")
        outlet_id = request.data.get("outlet_id")
        latitude = request.data.get("latitude")
        longitude = request.data.get("longitude")
        outlet = get_object_or_404(Outlet.objects, id=outlet_id, worker__phone_number=phone)

        visit = Visit(outlet=outlet, latitude=latitude, longitude=longitude)
        visit.save()
        serializer = VisitSerializer(visit)
        return Response(serializer.data, status=status.HTTP_200_OK)
