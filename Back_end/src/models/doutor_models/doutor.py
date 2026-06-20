from tortoise import fields
from tortoise.models import Model
from enum import Enum


class Especialidade(Enum):
    """
    Especialidades médicas disponiveis mp sistema.
    Aparece na tela de busca por especilidade do prototipo
    """
    CARDIOLOGIA = "cardiologia"
    ORTOPEDIA = "ortopedia"
    PEDIATRIA = "pediatria"
    CLINICO_GERAL = "clinico_geral"
    DERMATOLOGIA = "dermatologia"
    NEUROLOGIA = "neurologia"
    GINECOLOGIA = "ginecologia"
    PSIQUIATRIA = "psiquiatria"

class Sexo(Enum):
    MASCULINO = "masculino"
    FEMININO = "feminino"
    OUTRO = "outro"

class DoutorModel(Model):

    """
    Representa um doutor cadastrado no sistema Cuida mais
    """
    # Dados pessoais do doutor
    id = fields.UUIDFfield(pk =True) # Chave primária
    nome = fields.charfield(max_lenght = 255)
    cpf = fields.charfield(max_lenght = 11, unique =True)
    sexo  = fields.charfield(max_lenght =20)
    email = fields.charfield(max_lenght = 255,unique =True)
    senha_has = fields.charfield(max_lenght =255)
    data_nascimento = fields.datefield()
    telefone = fields.charfield(max_lenght = 20)
    clinica = fields.charfield(max_lenght = 255)
    especialidade = fields.charEnumfield(Especialidade)

    # Dados de localização do doutor
    clinica_nome = fields.charfield(max_lenght = 255)
    clinica_id_local = fields.charfield(max_leght = 255)

    # Controle do sistema

    ativo = fields.booleanfiel(defautl = True)
    criado_em = fields.datetimefield(auto_now_add =True)
    # auto_now_add=True → preenchido automaticamente com a data/hora do cadastro


    # Relacionamentos reversos

    # permite acessar doutor.consultas e doutor.relatorios.

    consultas : fields.ReverseRelation["ConsultaModel"]
    relatorios: fields.ReverseRelation["RelatorioModel"]


    class Meta:
        table = "doutores"
        # Define o nome da tabela no banco de dados
 