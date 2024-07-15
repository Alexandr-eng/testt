from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Worker, Store, Visit
from .serializers import StoreSerializer, VisitSerializer


class StoreListView(APIView):
    """
    List all stores for a given worker phone number.
    """

    def get(self, request):
        phone_number = request.headers.get('Authorization').split()[1]
        try:
            worker = Worker.objects.get(phone_number=phone_number)
        except Worker.DoesNotExist:
            return Response({"error": "Worker not found"}, status=status.HTTP_404_NOT_FOUND)

        stores = Store.objects.filter(worker=worker)
        if not stores.exists():
            return Response({"error": "No stores found for this worker"}, status=status.HTTP_404_NOT_FOUND)

        serializer = StoreSerializer(stores, many=True)
        return Response(serializer.data)


class VisitCreateView(APIView):
    """
    Create a new visit for a given store and worker.
    """

    def post(self, request):
        phone_number = request.headers.get('Authorization').split()[1]
        store_id = request.data.get('store_id')
        latitude = request.data.get('latitude')
        longitude = request.data.get('longitude')

        try:
            worker = Worker.objects.get(phone_number=phone_number)
            store = Store.objects.get(id=store_id, worker=worker)
        except (Worker.DoesNotExist, Store.DoesNotExist):
            return Response({"error": "Invalid worker or store"}, status=status.HTTP_400_BAD_REQUEST)

        visit = Visit.objects.create(store=store, worker=worker, latitude=latitude, longitude=longitude)
        serializer = VisitSerializer(visit)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
