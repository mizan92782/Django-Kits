from xml.dom import ValidationErr
from jsonschema import ValidationError
from rest_framework import serializers

from students.models import Father
from students.services import father_status


#!============ father

class FatherSerializer(serializers.ModelSerializer):
    status = serializers.SerializerMethodField(read_only=True)
    # to give defaultg value in serializer,re write the fields
    age = serializers.IntegerField(default=0,required=False)
    salary = serializers.IntegerField(default=0,required=False)

    class Meta:
        model = Father
        fields = ['id', 'name', 'age', 'salary', 'status']
    
    def validate_age(self,value):
        if value < 30 :
            raise serializers.ValidationError("age must be greate than 30")
        return value
    
            
    def get_status(self,obj):
        return father_status(obj)
        
    def create(self, validated_data):
        print("A father object create")
        return super().create(validated_data)
        
    
    def to_representation(self, instance):
        represent = super().to_representation(instance)
        
        represent["message"]="Student Father Information"
        return represent