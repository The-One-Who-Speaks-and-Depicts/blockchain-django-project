from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status

from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .models import Block
from .serializers import *


@api_view(['GET'])
def blocks_list(request):
    """
 List  block
 """
    if request.method == 'GET':
        data = []
        nextPage = 1
        previousPage = 1
        blocks = Block.objects.all()
        page = request.GET.get('page', 1)
        paginator = Paginator(blocks, 50)
        try:
            data = paginator.page(page)
        except PageNotAnInteger:
            data = paginator.page(1)
        except EmptyPage:
            data = paginator.page(paginator.num_pages)

        serializer = BlockSerializer(data,context={'request': request} ,many=True)
        if data.has_next():
            nextPage = data.next_page_number()
        if data.has_previous():
            previousPage = data.previous_page_number()

        return Response({'data': serializer.data , 'count': paginator.count, 'numpages' : paginator.num_pages, 'nextlink': '/api/blocks/?page=' + str(nextPage), 'prevlink': '/api/blocks/?page=' + str(previousPage)})

@api_view(['GET'])
def blocks_detail(request, height):
    """
 Retrieve, update or delete a customer by id/pk.
 """
    try:
        block = Block.objects.get(pk=height)
    except Block.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = BlockSerializer(block,context={'request': request})
        return Response(serializer.data)    