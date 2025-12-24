
from rest_framework import serializers
from django.db import transaction

from myapp.models import Address, Customer, Post, User, Book


class AddressSerializer(serializers.Serializer):
    city = serializers.CharField()
    zip_code  = serializers.CharField()


class UserRegisterSerializer(serializers.Serializer):
    """
    User Registration Serializer
    
    Fields:
    - email: unique email
    - password: min 8 chars
    - name: full name
    - phone: phone number
    - age: must be 18+
    - address: nested address object
    """

    email = serializers.EmailField(
        help_text="User email address (unique)"
    )
    password = serializers.CharField(
        write_only=True, min_length=8
    )
    name = serializers.CharField(max_length=40)
    phone = serializers.CharField()
    age = serializers.IntegerField()
    address = AddressSerializer(required=False)

    full_info = serializers.SerializerMethodField(read_only=True)

    # --
    # 
    # -------- field validation ----------
    def validate_age(self, value):
        if value < 18:
            raise serializers.ValidationError("Age must be 18+")
        return value
        
    # ---------- object validation ----------
    def validate(self, data):
        if data["name"].lower() == "admin":
            raise serializers.ValidationError("Name cannot be admin")
        return data

    # ---------- create ----------
    '''POST request
       → View (CreateAPIView)
       → serializer.is_valid()
       → serializer.save()
       → serializer.create()
       
       
       if no need customize then not need to user create: alos we can send custome respose using serializer'''
       
    def create(self, validated_data):
        if User.objects.filter(email=validated_data["email"]).exists():
            raise serializers.ValidationError("Email already exists")
        
            
        """
        transaction.atomic ensures:
        - User create
        - Customer create
        BOTH succeed or BOTH rollback
        """
        with transaction.atomic():

            user = User.objects.create_user(
                email=validated_data["email"],
                password=validated_data["password"]
            )
            
            # Create Customer linked to User
            address = Address.objects.create(
                city=validated_data["address"]["city"],
                zip_code =validated_data["address"]["zip_code"]
            )

            customer = Customer.objects.create(
                user=user,
                address = address,
                name=validated_data["name"],
                phone=validated_data["phone"],
                age=validated_data["age"]
            )

        return customer
        
        

    # ---------- update ----------
    def update(self, instance, validated_data):
        instance.name = validated_data.get("name", instance.name)
        instance.phone = validated_data.get("phone", instance.phone)

        if "email" in validated_data:
            instance.user.email = validated_data["email"]
            instance.user.save()

        instance.save()
        return instance

    # ---------- readonly ----------
    def get_full_info(self, obj):
        return f"{obj.name} - {obj.user.email}"

        
        
        
    # ---------- response format ----------
    def to_representation(self, instance):
        return {
            "user_id": instance.user.id,
            'user_email': instance.user.email,
            "user_name": instance.user.customer.name,
            "user_phone": instance.user.customer.phone,
            "user_age": instance.user.customer.age,
            "address_city": instance.address.city,
            "address_zip": instance.address.zip_code,
            "message": "User registration successful",
            "full_info": self.get_full_info(instance),
        }

        
        
class PostCreateSerializer(serializers.Serializer):
    title = serializers.CharField(max_length=200)
    content = serializers.CharField()

    def create(self, validated_data):
        return Post.objects.create(**validated_data)


class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = '__all__'
    #!================================================================================ best way to represet the data in responser
    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation['user'] = {
            'id': instance.user.id,
            'email': instance.user.email
        }
        
        representation['customer'] = {
            'id': instance.user.customer.id,
            'name': instance.user.customer.name,
            'phone': instance.user.customer.phone
        }
        return representation
