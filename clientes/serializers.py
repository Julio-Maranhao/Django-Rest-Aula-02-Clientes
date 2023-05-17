from rest_framework import serializers
from clientes.models import Cliente
from clientes.validators import *


class ClienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cliente
        fields = '__all__'
        
    def validate(self, data):
        if not is_cpf_valid(data['cpf']):
            raise serializers.ValidationError({'cpf': 'Número de CPF inválido'})
        if not is_nome_valid(data['nome']):
            raise serializers.ValidationError({'nome':'O campo Nome não aceita números ou caracteres especiais.'})
        if not is_rg_valid(data['rg']):
            raise serializers.ValidationError({'rg': 'O RG deve ter 9 digitos.'})
        if not is_cell_number_valid(data['celular']):
            raise serializers.ValidationError({'celular': 'O Celular deve ser do tipo 00 91234-1234.'})
        return data
