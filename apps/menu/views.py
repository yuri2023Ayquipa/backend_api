from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, generics
from rest_framework import permissions
from drf_yasg.utils import swagger_auto_schema
from rest_framework.authentication import TokenAuthentication
from apps.User.authenticacion_mixins import Authentication



from .models import Menu
from .serializers import MenuSerializer
from core.utils import generic_detail_view

# Create your views here.
class MenuViews(Authentication, APIView):
    permission_classes = [permissions.IsAuthenticated,]
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer
    authentication_classes = [TokenAuthentication]

    @swagger_auto_schema(
        security=[{'Token': []}]
    )

    def get (self, request, format=None):
        menus = Menu.objects.all()
        if menus.exists():
            result = []
            # Filtrar categorias principales
            main_menus= menus.filter(parent=None)
            for main_menu in main_menus:
                item = {
                    'id': main_menu.id,
                    'name': main_menu.name,
                    'slug' : main_menu.slug,
                    'sub_menus' : []
                }
                sub_menus = menus.filter(parent=main_menu)
                for sub_menu in sub_menus:
                    sub_item = {
                        'id': sub_menu.id,
                        'name': sub_menu.name,
                        'slug' : sub_menu.slug,
                    }
                    item['sub_menus'].append(sub_item)
                result.append(item)
            serializer = self.serializer_class(menus)
            return Response(result, status=status.HTTP_200_OK)
        else:
            return Response({'error': 'No categories found'}, status=status.HTTP_404_NOT_FOUND)
    
    @swagger_auto_schema(
        operation_description="Create a new menu",
        request_body=MenuSerializer,
        responses={201: MenuSerializer} 
    )

    def post(self, request, format=None):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"status": "success", "data": {"menu": serializer.data}}, status=status.HTTP_201_CREATED)
        else:
            return Response({"status": "fail", "message": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
        
class MenuDetail_views(Authentication, APIView):
    permission_classes = [permissions.AllowAny]
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer  # Corregido el error tipográfico

    def get_menu(self, pk):
        try:
            return Menu.objects.get(pk=pk)
        except Menu.DoesNotExist:
            return None
    
    def get(self, request, pk):
        menu = self.get_menu(pk=pk)
        if menu:
            result = {
                'id': menu.id,
                'name': menu.name,
                'slug': menu.slug,
                'sub_menus': []
            }
            sub_menus = Menu.objects.filter(parent=menu)
            for sub_menu in sub_menus:
                sub_item = {
                    'id': sub_menu.id,
                    'name': sub_menu.name,
                    'slug': sub_menu.slug,
                }
                result['sub_menus'].append(sub_item)
            return Response(result, status=status.HTTP_200_OK)
        else:
            return Response({'error': 'No categories found'}, status=status.HTTP_404_NOT_FOUND)

    def delete(self, request, pk):
        menu = self.get_menu(pk)
        if menu == None:
            return Response({"status": "fail", "message": f"Note with Id: {pk} not found"}, status=status.HTTP_404_NOT_FOUND)
        
        menu.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)



menu_detail_view = generic_detail_view(Menu, MenuSerializer)