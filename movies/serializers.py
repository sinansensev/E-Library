from rest_framework import fields, serializers
from .models import *
class BiyografikPDFModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = biyografik
        fields = '__all__'
class GerilimPDFModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = gerilim
        fields = '__all__'
class MaceraPDFModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = macera
        fields = '__all__'
class ChildPDFModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = cocukkitabi
        fields = '__all__'
class KurguPDFModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = books
        fields = '__all__'
class AksiyonPDFModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = aksiyon
        fields = '__all__'
class EducationPDFModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = education
        fields = '__all__'
class UserModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = books
        fields= '__all__'
class UserModelSerializer1(serializers.ModelSerializer):
    class Meta:
        model = cocukkitabi
        fields= '__all__'        

class UserModelSerializer2(serializers.ModelSerializer):
    class Meta:
        model = education
        fields= '__all__' 
class UserModelSerializer3(serializers.ModelSerializer):
    class Meta:
        model = macera
        fields= '__all__'  
class UserModelSerializer4(serializers.ModelSerializer):
    class Meta:
        model = gerilim
        fields= '__all__'  
class UserModelSerializer5(serializers.ModelSerializer):
    class Meta:
        model = biyografik
        fields= '__all__'    
class UserModelSerializer6(serializers.ModelSerializer):
    class Meta:
        model = aksiyon
        fields= '__all__'                           

class CombinedModelSerializer(serializers.Serializer):
    BilimKurgu = UserModelSerializer(many=True)
    CocukKitabi = UserModelSerializer1(many=True)
    Egitim = UserModelSerializer2(many=True)
    Macera = UserModelSerializer3(many=True)
    Gerilim = UserModelSerializer4(many=True)   
    Biyografik = UserModelSerializer5(many=True)
    Aksiyon = UserModelSerializer6(many=True)     