from pdb import post_mortem
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
from django.http import HttpResponse
from django.http import FileResponse
from django.shortcuts import get_object_or_404
from movies.forms import ReviewForm, RatingForm 
from django.shortcuts import render, get_object_or_404, redirect
from movies.models import education

from .serializers import EducationPDFModelSerializer
from .serializers import AksiyonPDFModelSerializer

class AksiyonDownloadPDFAPIView(APIView):
    def get(self, request, pk):
        bookt = get_object_or_404(aksiyon, pk=pk)

        if bookt.pdf:
            response = FileResponse(bookt.pdf, content_type='application/pdf')
            response['Content-Disposition'] = f'attachment; filename="{bookt.name}.pdf"'
            return response
        else:
            return Response({'error': 'PDF not found'}, status=status.HTTP_404_NOT_FOUND)
class EducationDownloadPDFAPIView(APIView):
    def get(self, request, pk):
        book = get_object_or_404(education, pk=pk)

        if book.pdf:
            response = FileResponse(book.pdf, content_type='application/pdf')
            response['Content-Disposition'] = f'attachment; filename="{book.name}.pdf"'
            return response
        else:
            return Response({'error': 'PDF not found'}, status=status.HTTP_404_NOT_FOUND)

class CombinedModelView(APIView):
    def get(self, request, format=None):
        model1_data = books.objects.all()
        model2_data = cocukkitabi.objects.all()
        model3_data = education.objects.all()
        model4_data = macera.objects.all()
        model5_data = gerilim.objects.all()
        model6_data = biyografik.objects.all()
        model7_data = aksiyon.objects.all() 
    
        
        serializer = CombinedModelSerializer({
            'BilimKurgu': UserModelSerializer(model1_data, many=True).data,
            'CocukKitabi': UserModelSerializer1(model2_data, many=True).data,
            'Egitim': UserModelSerializer2(model3_data, many=True).data,
            'Macera': UserModelSerializer3(model4_data, many=True).data,
            'Gerilim': UserModelSerializer4(model5_data, many=True).data,
            'Biyografik': UserModelSerializer5(model6_data, many=True).data,
            'Aksiyon': UserModelSerializer6(model7_data, many=True).data, 
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

def product_detail(request, id):
    print("asdhgadshsdh",id)
    book = get_object_or_404(education, pk=pk) 
    print(book)
    if request.method == 'POST':
        review_form = ReviewForm(request.POST)
        print("TEST: \n\n\n", review_form)
        rating_form = RatingForm(request.POST)

        if review_form.is_valid() and rating_form.is_valid():
            review = review_form.save(commit=False)
            review.user = request.user
            review.book = book
            review.save()

            rating = rating_form.save(commit=False)
            rating.user = request.user
            rating.book = book
            rating.save()

            return redirect('product_detail', product_id=id)
    else:
        review_form = ReviewForm()
        rating_form = RatingForm()

    return render(request, 'product.html', {'book': book, 'review_form': review_form, 'rating_form': rating_form})
