from rest_framework import fields, serializers
from .models import *
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
    model1 = UserModelSerializer(many=True)
    model2 = UserModelSerializer1(many=True)
    model3 = UserModelSerializer2(many=True)
    model4 = UserModelSerializer3(many=True)
    model5 = UserModelSerializer4(many=True)   
    model6 = UserModelSerializer5(many=True)
    model7 = UserModelSerializer6(many=True)     