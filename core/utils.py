from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

def generic_detail_view(model, serializer_class):
    @api_view(['GET', 'PUT', 'DELETE'])
    def view(request, pk):
        try:
            instance = model.objects.get(pk=pk)
        except model.DoesNotExist:
            return Response({'error': 'Not found'}, status=status.HTTP_404_NOT_FOUND)
        
        if request.method == 'GET':
            serializer = serializer_class(instance)
            return Response(serializer.data)
        elif request.method == 'PUT':
            serializer = serializer_class(instance, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors, statu=status.HTTP_400_BAD_REQUEST)
        elif request.method == 'DELETE':
            instance.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
    return view