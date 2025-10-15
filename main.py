from fastapi import FastAPI, Depends, Query, Request
from fastapi.responses import RedirectResponse
from pydantic import BaseModel
from sqlalchemy.orm import Session
from database import SessionLocal, engine, Base
from modelos import Medicion, MedicionCreate, Parametro

from modelos import EstadosResponse


app = FastAPI()
"""
@app.middleware("http")
async def allow_http_for_devices(request: Request, call_next):
    # Si la petición es HTTPS, continuar normal
    if request.url.scheme == "https":
        response = await call_next(request)
        return response

    # Si es HTTP (no segura)
    # Permitimos específicamente el endpoint /MEDICIONES
    if request.url.path == "/MEDICIONES" and request.method == "POST":
        print("⚠️  Petición HTTP permitida desde dispositivo SIM800L")
        response = await call_next(request)
        return response

    # Para todo lo demás, redirigir a HTTPS
    https_url = request.url.replace(scheme="https")
    return RedirectResponse(url=https_url)
"""
    
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


class Mediciones(BaseModel):
    valor_humedad: str
    valor_temperatura: str
    valor_conductividad: str
    valor_PH: str
    valor_nitrogeno: str
    valor_fosforo: str
    valor_potasio: str
    fecha: str
    hora: str

class EstadosResultado(BaseModel):
    tiempo_intervalo: str
    estado_riego: bool
    estado_sensores: bool

class EstadoParametro(BaseModel):
    COD_PARAMETRO: str
    DESC_PARAMETRO: str
    COD_ESTADO: str
    #DESC_ESTADO: str


    class Config:
        orm_mode = True
class ConsultaParametros(BaseModel):
    codigos: list[str]

"""
@app.post("/REGISTRO_SENSORES")
def REGISTRO_SENSORES():

    return "hola desde post python"
"""

@app.post("/CONSULTA_ESTADOS", response_model=list[EstadoParametro])
def obtener_estado_parametros(
    consulta: ConsultaParametros,
    db: Session = Depends(get_db)
):
    resultados = db.query(Parametro).filter(Parametro.COD_PARAMETRO.in_(consulta.codigos)).all()
    return resultados



@app.post("/MEDICIONES")
def crear_medicion(medicion: MedicionCreate, db: Session = Depends(get_db)):
    try: 
        db_medicion = Medicion(**medicion.dict())
        db.add(db_medicion)
        db.commit()
        db.refresh(db_medicion)
        return "Ingresado con exito"
    except Exception as e:
        return "El ingreso fallo" + str(e)
