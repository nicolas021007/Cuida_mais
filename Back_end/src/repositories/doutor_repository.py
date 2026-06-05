from models.doutor import DoutorModel
from domain.doutor import Doutor
from uuid import uuid4
from typing import List



class DoutorRepository:

    async def salvar_doutor(self, doutor: Doutor) -> DoutorModel:

        return await DoutorModel.create(
            id = str(uuid4()),
            nome = doutor.nome,
            crm = doutor.crm,
            especialidade = doutor.especialidade,
            telefone =  doutor.telefone,
            ativo = doutor.ativo,
            
        )

    async def buscar_por_id(self, id: str) ->DoutorModel:
        return await DoutorModel.get_or_none(id=id)

    async def listar_doutores(self) -> List[DoutorModel]:
        return await DoutorModel.all()

    async def listar_porespecialidade(self, especialidade: str) -> List[DoutorModel]:
        return await DoutorModel.filter(especialidade = especialidade).all()


        

    
















