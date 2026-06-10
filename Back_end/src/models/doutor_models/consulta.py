from tortoise import fields
from tortoise.models import Model
from enum import Enum

# Define o model de Consulta com banco de dados usando Tortoise ORM


class StatusConsulta(str, Enum):

    """
    Representa  o estado atual de uma consulta.

    Fluxo normal:
       Agendada -> Confirmada -> Concluida -> Cancelada
    """

    AGENDADA = "Agendada"
    CONFIRMADA = "Confirmada"
    CONCLUIDA = "Concluida"
    CANCELADA = "Cancelada"


class ConsultaModel(Model):

    """
    Representa uma consulta médica, agendada no sistema.

    Relacionamentos:
     - Pertence a um doutor (N:1)
     - Um doutor pode ter várias consultas (1:N)
    """


    id = fields.UUIDField(pk =True) 

    doutor = fields.ForeignKeyField(

        "models.DoutorModel",
        related_name = "Consultas",
        on_delete = fields.CASCADE   # Exclui consultas associadas se o doutor for excluido
    )

    paciente_nome = fields.CharField(max_length = 100)

    paciente_cpf = fields.CharField(max_length = 14)

    data_hora = fields.DateTimeField()
    duracao_minutos = fields.IntField(default = 30)

    motivo = fields.CharField(max_length = 200, default = "Consulta de rotina")

    observacoes = fields.TextField(default = "")

    status = fields.CharEnumField(StatusConsulta, default = StatusConsulta.AGENDADA)

    clinica_nome = fields.CharField(max_length = 100, default = "CLINICA SAÚDE")

    criado_em = fields.DateTimeField(auto_nowadd = True)

    class Meta:
        table = "consultas"

        #Nome da tabela no banco de dados