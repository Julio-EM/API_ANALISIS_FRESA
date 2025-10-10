import datetime
from typing import Optional
from pydantic import BaseModel
from sqlalchemy import Column, Integer, String, Float
from database import Base

class EstadosResponse(BaseModel):
    estadoRiego: str
    estadoMediciones: bool
    intervaloMediciones: bool

class Medicion(Base):
    __tablename__ = "MEDICION"
    
    ID_MEDICION = Column(Integer, primary_key=True, index=True)
    ID_SENSOR = Column(Float)
    HUMEDAD = Column(Float)
    TEMPERATURA = Column(Float)
    CONDUCTIVIDAD = Column(Float)
    PH = Column(Float)
    NITROGENO = Column(Float)
    FOSFORO = Column(Float)
    POTASIO = Column(Float)
    FECHA = Column(String(20))
    HORA = Column(String(20))

class Parametro(Base):
    __tablename__ = "PARAMETROS"

    ID_PARAMETRO = Column(Integer, primary_key=True, index=True)
    COD_PARAMETRO = Column(String(20), index=True)
    DESC_PARAMETRO = Column(String(50))
    COD_ESTADO = Column(String(10))
    DESC_ESTADO = Column(String(20))



# Modelo Pydantic
class MedicionCreate(BaseModel):
    ID_SENSOR: int
    HUMEDAD: float
    TEMPERATURA: float
    CONDUCTIVIDAD: float
    PH: float
    NITROGENO: float
    FOSFORO: float
    POTASIO: float
    FECHA: str
    HORA: str
