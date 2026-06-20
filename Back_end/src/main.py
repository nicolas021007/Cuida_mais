from contextlib import asynccontextmanager
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from tortoise.contrib.fastapi import RegisterTortoise
from api.route.doutores import router as doutores_router
from api.route.pacientes import router as pacientes_router
from api.route.pacientes import router as pacientes_router, set_db_pacientes
from database import TORTOISE_ORM


@asynccontextmanager
async def lifespan(app: FastAPI):
  async with RegisterTortoise(
    app, 
    config= TORTOISE_ORM
    generate_schemas=True,
    add_exception_handlers=True
  ):
    yield


app = FastAPI(
  title = "Mais Saúde",
  description = "Agendador de consultas médicas",
  version ="1.0.0",
  lifespan= lifespan


)