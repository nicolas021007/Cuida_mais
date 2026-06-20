from tortoise import fields
from tortoise.models import Model


class RelatorioModel(Model):
    """
    Representa um relatório de consulta criada pelo doutor.

    Baseado na tela "Criar Relatório da consulta" do protótipo .
    Após ser salvo, exibirá a mensagem : "Relatório criado com sucesso!" 

    Relacionamentos:
        - Pertence a um doutor (N:1)
        - Um doutor pode ter vários relatórios (1:N)

    """

    id = fields.UUIDFIELD(pk = True)

    # Chave estrangeira - Relacionamento com o Doutor
    doutor = fields.ForeignKeyField(

        "models.DoutorModel",
        related_name = "Relatorios",
        on_delete = fields.CASCADE
    )
    # Dados do paciente
    paciente_nome = fields.CharField(max_length = 100)
    paciente_cpf = fields.CharField(max_length = 14)

    # Conteúdo do relatório

    titulo = fields.CharField(max_length = 200)
    conteudo = fields.TextField()

    # Controle do sistema
    criado_em = fields.DateTimeField(auto_now_add = True)

    class Meta: 
        table = "relatorios"
        