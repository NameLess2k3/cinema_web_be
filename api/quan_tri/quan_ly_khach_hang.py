from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

@api_view(['GET', 'POST'])
def customer_info_view(request):
    if request.method == 'GET':
        # Logic for retrieving customer info
        return Response({"message": "Retrieved customer info"}, status=status.HTTP_200_OK)
    elif request.method == 'POST':
        # Logic for storing or updating customer info
        return Response({"message": "Customer info updated"}, status=status.HTTP_201_CREATED)

@api_view(['GET', 'POST'])
def invoice_management_view(request):
    if request.method == 'GET':
        # Logic for retrieving invoice info
        return Response({"message": "Retrieved invoice info"}, status=status.HTTP_200_OK)
    elif request.method == 'POST':
        # Logic for storing or updating invoice info
        return Response({"message": "Invoice info updated"}, status=status.HTTP_201_CREATED)

@api_view(['GET', 'POST'])
def promotion_management_view(request):
    if request.method == 'GET':
        # Logic for retrieving promotion info
        return Response({"message": "Retrieved promotion info"}, status=status.HTTP_200_OK)
    elif request.method == 'POST':
        # Logic for storing or updating promotion info
        return Response({"message": "Promotion info updated"}, status=status.HTTP_201_CREATED)

