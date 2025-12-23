from rest_framework import serializers
from MyAuth.models import User, Customer


class AddressSerializer(serializers.Serializer):
    city = serializers.CharField()
    zip = serializers.CharField()


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

    email = serializers.EmailField(a
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

    # ---------- field validation ----------
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

            customer = Customer.objects.create(
                user=user,
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
            "email": instance.user.email,
            "name": instance.name,
            "phone": instance.phone,
            "age": instance.age,
            "full_info": self.get_full_info(instance),
        }
        
