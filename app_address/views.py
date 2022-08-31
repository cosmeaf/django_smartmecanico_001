from .models import Address
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import status
from .serializers import AddressSerializer

# ViewSets define the view behavior.


class AddressViewSet(viewsets.GenericViewSet):
    """ ViewSets Version 1 """
    model = Address
    serializer_class = AddressSerializer
    # queryset = Address.objects.all()

    def get_queryset(self, pk=None):
        if pk is None:
            return self.get_serializer().Meta.model.objects.all()
        return self.get_serializer().Meta.model.objects.filter(id=pk, is_active=True).first()

    def list(self, request):
        serializer = self.get_serializer(self.get_queryset(), many=True)
        return Response(serializer.data)

    def create(self, request, *args, **kwargs):
        print(request.data)
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'message': 'Address created Successfully'}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # def retrieve(self, request, pk=None):
    #     pass

    def update(self, request, pk=None):
        if self.get_queryset(pk):
            address_serializer = self.serializer_class(
                self.get_queryset(pk), data=request.data)
            if address_serializer.is_valid():
                return Response(address_serializer.data, status=status.HTTP_200_OK)
            return Response(address_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # def partial_update(self, request, pk=None):
    #     pass

    def destroy(self, request, pk=None):
        queryset = Address.objects.filter(id=pk).first()
        if queryset:
            queryset.is_active = False
            queryset.save()
            return Response({'message': 'Addres Removed Successfully'}, status=status.HTTP_200_OK)
        return Response({'message': 'Ops! Address not found'}, status=status.HTTP_400_BAD_REQUEST)