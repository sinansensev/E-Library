from django.shortcuts import render
from movies.models import *
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import *
from rest_framework import viewsets
from .serializers import *
from rest_framework.views import APIView
from rest_framework.response import Response

class CombinedModelView(APIView):
    def get(self, request, format=None):
        model1_data = books.objects.all()
        model2_data = cocukkitabi.objects.all()
        model3_data = education.objects.all()
    
        
        serializer = CombinedModelSerializer({
            'model1': UserModelSerializer(model1_data, many=True).data,
            'model2': UserModelSerializer1(model2_data, many=True).data,
            'model3': UserModelSerializer2(model3_data, many=True).data,
        })

        return Response(serializer.data)

    def post(self, request, format=None):
        model_name = request.data.get('model_name', None)

        if model_name == 'books':
            serializer = UserModelSerializer(data=request.data.get('data', {}))
        elif model_name == 'cocukkitabi':
            serializer = UserModelSerializer1(data=request.data.get('data', {}))
        elif model_name == 'education':
            serializer = UserModelSerializer2(data=request.data.get('data', {}))
        elif model_name == 'macera':
            serializer = UserModelSerializer3(data=request.data.get('data', {}))
        elif model_name == 'gerilim':
            serializer = UserModelSerializer4(data=request.data.get('data', {}))   
        elif model_name == 'biyografik':
            serializer = UserModelSerializer5(data=request.data.get('data', {}))   
        elif model_name == 'aksiyon':
            serializer = UserModelSerializer6(data=request.data.get('data', {}))            
        else:
            return Response({'error': 'Invalid model_name'}, status=status.HTTP_400_BAD_REQUEST)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class CombinedModelViewSet(viewsets.ModelViewSet):
    queryset = books.objects.all()
    serializer_class = UserModelSerializer
    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)
class Model2ViewSet(viewsets.ModelViewSet):
    queryset = cocukkitabi.objects.all()
    serializer_class = UserModelSerializer1
class Model3ViewSet(viewsets.ModelViewSet):
    queryset = education.objects.all()
    serializer_class = UserModelSerializer2 

class Model4ViewSet(viewsets.ModelViewSet):
    queryset = macera.objects.all()
    serializer_class = UserModelSerializer3

class Model5ViewSet(viewsets.ModelViewSet):
    queryset = gerilim.objects.all()
    serializer_class = UserModelSerializer4        
class Model6ViewSet(viewsets.ModelViewSet):
    queryset = biyografik.objects.all()
    serializer_class = UserModelSerializer5    
class Model7ViewSet(viewsets.ModelViewSet):
    queryset = aksiyon.objects.all()
    serializer_class = UserModelSerializer6
# Create your views here.
"""kategori_liste = ["macera","romantik","dram","bilim kurgu"]
film_liste =[
    {
        "film_adi" : "film 1",
        "aciklama" : "film 1 açıklama",
        "resim" : "1.jpeg",
        "anasayfa": True
    },
     { "film_adi" : "film 2",
        "aciklama" : "film 2 açıklama",
        "resim" : "2.jpeg",
        "anasayfa": False
       },
    {
        "film_adi" : "film 3",
        "aciklama" : "film 3 açıklama",
        "resim" : "3.jpeg",
        "anasayfa": True
    }   
    ]
"""
"""def home(request):
    data = {
        "kategoriler" : kategori_liste,
        "filmler" : film_liste 
    }
    return render(request,"index.html",data)
def movies(request):
    data = {
        "kategoriler" : kategori_liste,
        "filmler" : film_liste 
    }
    #sorgu=books.objects.filter(name="sinan")
    #sorgu="asd"
    #sorgu.save()
    return render(request,"movies.html",data)"""    
