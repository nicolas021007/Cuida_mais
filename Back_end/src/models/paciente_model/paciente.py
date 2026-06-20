from tortoise import fields
from tortoise.models import Model
from enum import Enum


class Sexo(str, Enum):
    MASCULINO = "Masculino"
    FEMINIO = "Feminino"
    OUTRO = "Outro"
    NAO_INFORMADO = "nao_informado"


class PacienteModel(Model):
    """Args:
    Criando o modelo de banco pro Paciente.
    """

    cpf = fields.CharField(primary_key = True, max_lenght = 14)
    nome = fields.CharField(max_lenght = 100)
    data_nascimento = fields.DateField()
    sexo = fields.CharEnumField(Sexo)
    cep = fields.CharField(max_lenght = 9)
    logradouro = fields.CharField(max_lenght = 200)
    bairro = fields.CharField(max_lenght = 100)
    cidade = fields.CharField(max_lenght = 100)
    estado = fields.CharField(max_lenght = 2)
    numero = fields.CharField(max_lenght = 10)
    complemento = fields.CharField(max_lenght = 100, default = "")
    ativo = fields.BooleanField(default =  True)

    class Meta:
        table = "pacientes"