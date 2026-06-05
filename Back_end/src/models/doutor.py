from tortoise import fields
from tortoise.models import Model
from enum import Enum


class Especialidade(Enum):
    CARDIOLOGIA = "cardiologia"
    ORTOPEDIA = "ortopedia"
    PEDIATRIA = "pediatria"
    CLINICO_GERAL = "clinico_geral"

class DoutorModel(Model):
    id = fields.IntField(primary_key = True)
    nome = fields.CharField(max_length = 100)
    crm = fields.CharField(max_length = 20, unique =True)
    telefone = fields.CharField(max_length =20)
    especialidade = fields.CharEnumField(Especialidade)

    class Meta:
        table = "doutores"