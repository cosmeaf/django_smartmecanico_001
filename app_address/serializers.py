from .models import Address
from rest_framework import serializers
from smartmecanico.serializers import UserSerializer


class AddressSerializer(serializers.ModelSerializer):
    # user = serializers.StringRelatedField(read_only=True)
    # user = serializers.PrimaryKeyRelatedField(read_only=True)

    class Meta:
        model = Address
        fields = '__all__'
        depth = 1

# class AddressSerializer(serializers.ModelSerializer):
#     # Metodo para representar relacionamento
#     # user = serializers.StringRelatedField()

#     class Meta:
#         model = Address
#         fields = '__all__'
#         # depth = 1
#         read_only_fields = ('created_at', 'updated_at', 'deleted_at')

    # def to_representation(self, instance):
    #     self.fields['user'] = UserSerializer(read_only=True)
    #     return super(AddressSerializer, self).to_representation(instance)

    # def to_representation(self, instance):
    #     self.fields['user'] = UserSerializer(read_only=True)
    #     return {
    #         'id': instance.id,
    #         'cep': instance.cep,
    #         'logradouro': instance.logradouro,
    #         'complemento': instance.complemento,
    #         'bairro': instance.bairro,
    #         'localidade': instance.localidade,
    #         'uf': instance.uf,
    #         'user': instance.user_id
    #     }
