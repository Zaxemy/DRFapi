from django.shortcuts import render
from rest_framework import generics, viewsets
from women.models import Women, Category
from women.serializers import WomenSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from django.forms import model_to_dict
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAdminUser, IsAuthenticated
from women.permissions import IsAdminOrReadOnly, IsOwnerOrReadOnly


class WomenAPIList(generics.ListCreateAPIView):
    queryset = Women.objects.all()
    serializer_class = WomenSerializer
    permission_classes = (IsAuthenticatedOrReadOnly, )
    
    
    
class WomenAPIDestroy(generics.RetrieveDestroyAPIView):
    queryset = Women.objects.all()
    serializer_class = WomenSerializer
    permission_classes = (IsAdminOrReadOnly, )
    
    
    
class WomenAPIUpdate(generics.RetrieveUpdateAPIView):
    queryset = Women.objects.all()
    serializer_class = WomenSerializer
    permission_classes = (IsOwnerOrReadOnly,)
    

    









# class WomenAPIView(APIView):
#     def get(self, request):
#         women = Women.objects.all()
#         return Response({'get': WomenSerializer(women, many=True).data})
    
    
#     def post(self, request):
#         serializer = WomenSerializer(data=request.data)
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
        
#         return Response({"post": serializer.data})
    
    # def put(self, request, *args, **kwargs):
    #     pk = kwargs.get("pk", None)
    #     if not pk:
    #         return Response({"error": "Method PUT not allowed"})
        
    #     try:
    #         instance = Women.objects.get(pk=pk)
    #     except:
    #         return Response({"error": "Object does not exists"})
        
    #     serializer = WomenSerializer(data=request.data, instance=instance)
    #     serializer.is_valid(raise_exception=True)
    #     serializer.save()
    #     return Response({"post": serializer.data})
    
    
    

        
        

    
    
